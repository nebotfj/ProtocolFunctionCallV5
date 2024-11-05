"""Balancer Protocol Functions"""

BALANCER_FUNCTIONS = {
    'POOL': {
        'joinPool': 'OUTGOING',
        'exitPool': 'INCOMING',
        'swap': 'BOTH',
        'batchSwap': 'BOTH'
    },
    'LIQUIDITY': {
        'provideLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING',
        'createPool': 'OUTGOING',
        'setSwapFee': 'OUTGOING'
    },
    'STAKING': {
        'stake': 'OUTGOING',
        'unstake': 'INCOMING',
        'getReward': 'INCOMING',
        'exit': 'INCOMING'
    }
}