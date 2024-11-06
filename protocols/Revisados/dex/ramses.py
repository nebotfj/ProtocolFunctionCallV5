"""Ramses Exchange Protocol Functions"""

RAMSES_FUNCTIONS = {
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
        'stakeRAM': 'OUTGOING',
        'unstakeRAM': 'INCOMING',
        'claimRewards': 'INCOMING',
        'compoundRewards': 'OUTGOING'
    },
    'BRIBES': {
        'addBribe': 'OUTGOING',
        'claimBribe': 'INCOMING',
        'voteBribe': 'OUTGOING'
    }
}