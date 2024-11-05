"""Curve Protocol Functions"""

CURVE_FUNCTIONS = {
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
    },
    'STAKING': {
        'stake': 'OUTGOING',
        'unstake': 'INCOMING',
        'claim': 'INCOMING',
        'vote_for_gauge_weights': 'OUTGOING',
        'deposit_reward_token': 'OUTGOING'
    }
}