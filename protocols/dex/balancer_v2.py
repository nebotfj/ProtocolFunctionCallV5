"""Balancer V2 Protocol Functions"""

BALANCER_V2_FUNCTIONS = {
    'TRADING': {
        'swap': 'BOTH',
        'batchSwap': 'BOTH',
        'flashSwap': 'BOTH',
        'querySwap': 'NEUTRAL'
    },
    'LIQUIDITY': {
        'joinPool': 'OUTGOING',
        'exitPool': 'INCOMING',
        'manageUserBalance': 'BOTH',
        'managePoolBalance': 'BOTH'
    },
    'WEIGHTED_POOL': {
        'create': 'OUTGOING',
        'updateWeightsGradually': 'OUTGOING',
        'updateSwapFee': 'OUTGOING'
    },
    'STABLE_POOL': {
        'createStablePool': 'OUTGOING',
        'setAmplificationParameter': 'OUTGOING'
    },
    'BOOSTED_POOL': {
        'createBoostedPool': 'OUTGOING',
        'setBoostedPoolParameters': 'OUTGOING'
    }
}