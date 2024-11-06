"""Dystopia Protocol Functions"""

DYSTOPIA_FUNCTIONS = {
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
        'removeLiquidityETH': 'INCOMING',
        'mintLPToken': 'OUTGOING',
        'burnLPToken': 'INCOMING'
    },
    'STAKING': {
        'stakeDYST': 'OUTGOING',
        'unstakeDYST': 'INCOMING',
        'claimRewards': 'INCOMING',
        'stakeLPToken': 'OUTGOING',
        'unstakeLPToken': 'INCOMING'
    },
    'BRIBES': {
        'addBribe': 'OUTGOING',
        'claimBribe': 'INCOMING',
        'getBribesForEpoch': 'NEUTRAL'
    }
}