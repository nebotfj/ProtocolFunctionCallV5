"""BiSwap Protocol Functions"""

BISWAP_FUNCTIONS = {
    'SWAP': {
        'swapExactTokensForTokens': 'BOTH',
        'swapTokensForExactTokens': 'BOTH',
        'swapExactBNBForTokens': 'OUTGOING',
        'swapTokensForExactBNB': 'BOTH'
    },
    'LIQUIDITY': {
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING',
        'addLiquidityBNB': 'OUTGOING',
        'removeLiquidityBNB': 'INCOMING'
    },
    'FARMING': {
        'deposit': 'OUTGOING',
        'withdraw': 'INCOMING',
        'harvest': 'INCOMING',
        'emergencyWithdraw': 'INCOMING'
    },
    'LAUNCHPAD': {
        'participate': 'OUTGOING',
        'harvest': 'INCOMING',
        'emergencyWithdraw': 'INCOMING'
    }
}