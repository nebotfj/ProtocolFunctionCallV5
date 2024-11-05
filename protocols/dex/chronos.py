"""Chronos Protocol Functions"""

CHRONOS_FUNCTIONS = {
    'TRADING': {
        'swapExactTokensForTokens': 'BOTH',
        'swapTokensForExactTokens': 'BOTH',
        'swapExactETHForTokens': 'OUTGOING',
        'swapTokensForExactETH': 'BOTH'
    },
    'LIQUIDITY': {
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING',
        'addLiquidityETH': 'OUTGOING',
        'removeLiquidityETH': 'INCOMING'
    },
    'STAKING': {
        'stakeCHR': 'OUTGOING',
        'unstakeCHR': 'INCOMING',
        'claimRewards': 'INCOMING',
        'compoundRewards': 'OUTGOING'
    }
}