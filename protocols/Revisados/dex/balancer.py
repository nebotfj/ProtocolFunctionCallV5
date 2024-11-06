"""Balancer Protocol Functions for all versions"""

BALANCER_V1_FUNCTIONS = {
    'POOL': {
        'joinPool': 'OUTGOING',
        'exitPool': 'INCOMING',
        'swapExactAmountIn': 'BOTH',
        'swapExactAmountOut': 'BOTH'
    },
    'SMART_POOLS': {
        'updateWeight': 'OUTGOING',
        'updateWeightsGradually': 'OUTGOING',
        'pokeWeights': 'OUTGOING'
    }
}

BALANCER_V2_FUNCTIONS = {
    'VAULT': {
        'swap': 'BOTH',
        'batchSwap': 'BOTH',
        'joinPool': 'OUTGOING',
        'exitPool': 'INCOMING',
        'flashLoan': 'BOTH'
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
        'provideLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING',
        'createPool': 'OUTGOING',
        'setSwapFee': 'OUTGOING'
    },

    
    'BOOSTED_POOL': {
        'createBoostedPool': 'OUTGOING',
        'setBoostedPoolParameters': 'OUTGOING'
    }
}




# Combined functions for all versions
BALANCER_FUNCTIONS = {
    'V1': BALANCER_V1_FUNCTIONS,
    'V2': BALANCER_V2_FUNCTIONS,
    'COMMON': {
        'STAKING': {
            'stake': 'OUTGOING',
            'unstake': 'INCOMING',
            'getReward': 'INCOMING',
            'exit': 'INCOMING'
        }
    }
}