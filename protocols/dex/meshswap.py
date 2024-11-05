"""Meshswap Protocol Functions"""

MESHSWAP_FUNCTIONS = {
    'TRADING': {
        'swapExactTokensForTokens': 'BOTH',
        'swapTokensForExactTokens': 'BOTH',
        'swapExactMATICForTokens': 'OUTGOING',
        'swapTokensForExactMATIC': 'BOTH'
    },
    'LIQUIDITY': {
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING',
        'addLiquidityMATIC': 'OUTGOING',
        'removeLiquidityMATIC': 'INCOMING',
        'mintLPToken': 'OUTGOING',
        'burnLPToken': 'INCOMING'
    },
    'FARMING': {
        'stakeLPTokens': 'OUTGOING',
        'unstakeLPTokens': 'INCOMING',
        'harvestRewards': 'INCOMING',
        'compoundRewards': 'OUTGOING'
    }
}