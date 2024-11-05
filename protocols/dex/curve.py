"""Curve Protocol Functions for all versions"""

CURVE_V1_FUNCTIONS = {
    'POOL': {
        'add_liquidity': 'OUTGOING',
        'remove_liquidity': 'INCOMING',
        'remove_liquidity_one_coin': 'INCOMING',
        'exchange': 'BOTH',
        'exchange_underlying': 'BOTH'
    },
    'GAUGE': {
        'deposit': 'OUTGOING',
        'withdraw': 'INCOMING',
        'claim_rewards': 'INCOMING',
        'mint': 'OUTGOING',
        'mint_many': 'OUTGOING'
    }
}

CURVE_V2_FUNCTIONS = {
    'POOL': {
        'add_liquidity': 'OUTGOING',
        'remove_liquidity': 'INCOMING',
        'exchange': 'BOTH',
        'exchange_underlying': 'BOTH',
        'add_liquidity_one_coin': 'OUTGOING',
        'remove_liquidity_one_coin': 'INCOMING'
    },
    'TRICRYPTO': {
        'exchange': 'BOTH',
        'exchange_underlying': 'BOTH',
        'add_liquidity': 'OUTGOING',
        'remove_liquidity_one_coin': 'INCOMING'
    },
    'FACTORY': {
        'deploy_pool': 'OUTGOING',
        'deploy_metapool': 'OUTGOING',
        'set_fee_receiver': 'OUTGOING'
    }
}

# Combined functions for all versions
CURVE_FUNCTIONS = {
    'V1': CURVE_V1_FUNCTIONS,
    'V2': CURVE_V2_FUNCTIONS,
    'COMMON': {
        'STAKING': {
            'stake': 'OUTGOING',
            'unstake': 'INCOMING',
            'claim': 'INCOMING',
            'vote_for_gauge_weights': 'OUTGOING',
            'deposit_reward_token': 'OUTGOING'
        }
    }
}