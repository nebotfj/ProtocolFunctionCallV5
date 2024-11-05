"""MixSwap Protocol Functions"""

MIXSWAP_FUNCTIONS = {
    'TRADING': {
        'swap': 'BOTH',
        'multiSwap': 'BOTH',
        'flashSwap': 'BOTH',
        'routeSwap': 'BOTH'
    },
    'LIQUIDITY': {
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING',
        'zapIn': 'OUTGOING',
        'zapOut': 'INCOMING'
    },
    'FARMING': {
        'stake': 'OUTGOING',
        'unstake': 'INCOMING',
        'harvest': 'INCOMING'
    }
}