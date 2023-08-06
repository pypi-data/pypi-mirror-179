import json
import os
from dateutil.relativedelta import relativedelta
from .transaction import Transaction
from .node import ConcordiumNode
from .ccdscan import CCDScan
from .mongodb import MongoDB
from enum import Enum
import datetime as dt
import dateutil
from datetime import timezone

class SubscriptionDetails(Enum):
    EXPLORER_CCD                = os.environ.get('EXPLORER_CCD', '3cunMsEt2M3o9Rwgs2pNdsCWZKB5MkhcVbQheFHrvjjcRLSoGP')
    BAKER_ID                    = int(os.environ.get('BAKER_ID', 72723))
    SUBSCRIPTION_ONE_TIME_FEE   = int(os.environ.get('SUBSCRIPTION_ONE_TIME_FEE', 1000))
    SUBSCRIPTION_MESSAGE_CREDITS_IN_FEE    = int(os.environ.get('SUBSCRIPTION_MESSAGE_CREDITS_IN_FEE', 50))
    SUBSCRIPTION_MESSAGE_FEE    = int(os.environ.get('SUBSCRIPTION_MESSAGE_FEE', 1))
    SUBSCRIPTION_UNLIMITED      = int(os.environ.get('SUBSCRIPTION_UNLIMITED', 5000))
    SUBSCRIPTION_DELEGATOR_STAKE_LIMIT = int(os.environ.get('SUBSCRIPTION_DELEGATOR_STAKE_LIMIT', 100_000))

    # note that is this is True, 'test_user' test will fail in its current form...
    SUBSCRIPTION_PLAN_ACTIVE    = os.environ.get('SUBSCRIPTION_PLAN_ACTIVE', True)
    SUBSCRIPTION_PLAN_START_DATE = dateutil.parser.parse(os.environ.get('SUBSCRIPTION_PLAN_START_DATE', "2022-12-01 01:00:00")).astimezone(timezone.utc)
    SUBSCRIPTION_PLAN_COUNTDOWN = SUBSCRIPTION_PLAN_ACTIVE and (SUBSCRIPTION_PLAN_START_DATE >  dt.datetime.now().astimezone(timezone.utc))
    SUBSCRIPTION_PLAN_GO        = SUBSCRIPTION_PLAN_ACTIVE and (SUBSCRIPTION_PLAN_START_DATE <= dt.datetime.now().astimezone(timezone.utc))

class SubscriptionPlans(Enum):
    NO_PLAN = 'No Plan'
    PLUS = 'Plus'
    DELEGATION = 'Delegation'
    UNLIMITED = 'Unlimited'
class Subscription:
    def __init__(self):
        self.start_date             = None
        self.payment_transactions   = []
        self.subscription_active    = False # If True, the user has paid enough to pay for one-time fee
        self.delegator_active       = False # If True, the user has paid any amount from an account that is an active delegator
        self.site_active            = False # This is the indicator that a user can use the site
        self.bot_active             = False # If True, the user has paid enough to cover the one-time fee and sent messages
        self.unlimited              = False # If True, the user has paid enough for subscription_unlimited
        self.unlimited_end_date     = None
        self.remaining_message_credits = 0
        self.count_messages         = 0
        self.paid_amount            = 0
        self.plan                   = SubscriptionPlans.NO_PLAN

class User:
    def __init__(self):
        self.bakers_to_follow = []
        self.tags = {}
        
    def add_user_from_telegram(self, user):
        self.first_name = user.first_name
        self.username = user.username
        self.chat_id = user.id
        self.language_code = user.language_code
        return self

        
    def read_user_from_git(self, user):
        self.bakers_to_follow               = user.get('bakers_to_follow', [])
        self.chat_id                        = user.get('chat_id', None)
        self.token                          = user.get('token', None)
        self.first_name                     = user.get('first_name', None)
        self.username                       = user.get('username', None)
        self.accounts_to_follow             = user.get('accounts_to_follow', [])
        self.labels                         = user.get('labels', None)
        self.transactions_downloaded        = user.get('transactions_downloaded', {})
        self.transaction_limit_notifier     = user.get('transaction_limit_notifier', -1)
        self.smart_init                     = user.get('smart_init', False)
        self.smart_update                   = user.get('smart_update', False)
        self.cns_domain                     = user.get('cns_domain', False)
        self.nodes                          = user.get('nodes', {})
        self.subscription                   = Subscription()
        return self

    def perform_subscription_logic(self, 
        ccdscan: CCDScan, 
        node: ConcordiumNode, 
        mongodb: MongoDB, 
        ENVIRONMENT: str
        ):
        
        # payment_memo = 'coffee'
        payment_memo = self.token[:6]
        
        # get transactions sent to EXPLORER.CCD
        explorer_ccd_transactions, _ = ccdscan.ql_get_all_transactions_for_explorer_ccd(None, SubscriptionDetails.EXPLORER_CCD.value)
        explorer_ccd_transactions = [x['node']['transaction'] for x in explorer_ccd_transactions]
        
        # get delegators to EXPLORER.CCD (72723)
        explorer_ccd_delegators, _ = ccdscan.ql_get_all_delegators_for_explorer_ccd(None, SubscriptionDetails.BAKER_ID.value)
        # keyed on accountAddress
        explorer_ccd_delegators = {x['node']['accountAddress']['asString']: x['node'] for x in explorer_ccd_delegators}
        
        # check if the right memo is set, if so, count towards user.
        payment_txs = []
        paid_amount = 0
        SUBSCRIPTION_ONE_TIME_FEE_set = False
        ACTIVE_DELEGATOR_set          = False

        for tx in explorer_ccd_transactions:
            concordium_tx = Transaction(node).init_from_graphQL(tx).find_memo_and_amount()
            if concordium_tx.memo:
                if payment_memo in concordium_tx.memo:
                    paid_amount += concordium_tx.amount/1_000_000

                    # Is this sender a current active delegator?
                    if not ACTIVE_DELEGATOR_set:
                        if concordium_tx.sender in explorer_ccd_delegators:
                            sender_delegated_stake = explorer_ccd_delegators[concordium_tx.sender]['stakedAmount'] / 1_000_000
                            self.subscription.delegator_active = sender_delegated_stake >= SubscriptionDetails.SUBSCRIPTION_DELEGATOR_STAKE_LIMIT.value
                            
                            # Make sure that multiple transactions to not UNset this if later transactions make this invalid.
                            if self.subscription.delegator_active:
                                ACTIVE_DELEGATOR_set = True
                                self.subscription.plan = SubscriptionPlans.DELEGATION

                    # Has the user paid the one time fee? If so, record the subscription start date
                    if not SUBSCRIPTION_ONE_TIME_FEE_set:
                        self.subscription.subscription_active = paid_amount >= SubscriptionDetails.SUBSCRIPTION_ONE_TIME_FEE.value
                        
                        # Make sure that multiple transactions to not UNset this if later transactions make this invalid.
                        if self.subscription.subscription_active:
                            SUBSCRIPTION_ONE_TIME_FEE_set = True
                            self.subscription.plan = SubscriptionPlans.PLUS
                            
                            if isinstance(concordium_tx.block['blockSlotTime'], dt.datetime):
                                blockSlotTime = concordium_tx.block['blockSlotTime']
                            else:
                                blockSlotTime = dateutil.parser.parse(concordium_tx.block['blockSlotTime'])
                            
                            # some users have purchased before the official start date.
                            self.subscription.start_date = max(SubscriptionDetails.SUBSCRIPTION_PLAN_START_DATE.value, blockSlotTime)

                    # Has the user paid enough for unlimited? If so, record the unlimited end date
                    self.subscription.unlimited = paid_amount >= SubscriptionDetails.SUBSCRIPTION_UNLIMITED.value
                    if self.subscription.unlimited:
                        self.subscription.plan = SubscriptionPlans.UNLIMITED
                        if isinstance(concordium_tx.block['blockSlotTime'], dt.datetime):
                            self.subscription.unlimited_end_date = concordium_tx.block['blockSlotTime'] + relativedelta(years=1)
                        else:
                            self.subscription.unlimited_end_date = dateutil.parser.parse(concordium_tx.block['blockSlotTime']) + relativedelta(years=1)
                    payment_txs.append(concordium_tx)

        self.subscription.payment_transactions = payment_txs
        self.subscription.paid_amount = paid_amount

        # This is the indicator that a user can use the site. 
        self.subscription.site_active = self.subscription.delegator_active or self.subscription.subscription_active

        # get count of messages sent to this user
        # only count from subscription.start_date
        if self.subscription.start_date:
            try:
                pipeline = mongodb.get_bot_messages_for_user(self, ENVIRONMENT, self.subscription.start_date)
                result = list(mongodb.collection_messages.aggregate(pipeline))
                
                self.subscription.count_messages = 0
                if len (result) > 0:
                    if 'count_messages' in result[0]:
                        self.subscription.count_messages = result[0]['count_messages']
            except:
                pass

        self.subscription.remaining_message_credits = max(0, 
            (self.subscription.paid_amount - SubscriptionDetails.SUBSCRIPTION_ONE_TIME_FEE.value) / \
             SubscriptionDetails.SUBSCRIPTION_MESSAGE_FEE.value - \
             self.subscription.count_messages + \
            SubscriptionDetails.SUBSCRIPTION_MESSAGE_CREDITS_IN_FEE.value)
               

        if self.subscription.site_active:
            if self.subscription.remaining_message_credits > 0:
                self.subscription.bot_active = True
            else:
                self.subscription.bot_active = False

        # needed for parameterized test 'test_user'. 
        if not SubscriptionDetails.SUBSCRIPTION_PLAN_ACTIVE.value:
            self.subscription.bot_active = True

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)