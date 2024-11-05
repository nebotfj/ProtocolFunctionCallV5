"""Multichain (Anyswap) Bridge Protocol Functions"""

MULTICHAIN_FUNCTIONS = {
    'BRIDGE': {
        'anySwapOut': 'OUTGOING',
        'anySwapIn': 'INCOMING',
        'anySwapOutNative': 'OUTGOING',
        'anySwapInNative': 'INCOMING'
    },
    'ROUTER': {
        'swapExactTokensForTokens': 'BOTH',
        'swapTokensForExactTokens': 'BOTH',
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING'
    },
    'FARMING': {
        'stake': 'OUTGOING',
        'unstake': 'INCOMING',
        'getReward': 'INCOMING',
        'compound': 'OUTGOING'
    }
}