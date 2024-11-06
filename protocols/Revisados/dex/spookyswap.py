"""SpookySwap Protocol Functions"""

SPOOKYSWAP_FUNCTIONS = {
    'TRADING': {
        'swapExactTokensForTokens': 'BOTH',
        'swapTokensForExactTokens': 'BOTH',
        'swapExactFTMForTokens': 'OUTGOING',
        'swapTokensForExactFTM': 'BOTH'
    },
    'LIQUIDITY': {
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING',
        'addLiquidityFTM': 'OUTGOING',
        'removeLiquidityFTM': 'INCOMING'
    },
    'FARMING': {
        'deposit': 'OUTGOING',
        'withdraw': 'INCOMING',
        'harvest': 'INCOMING',
        'compound': 'OUTGOING'
    },
    'STAKING': {
        'stakeBOO': 'OUTGOING',
        'unstakeBOO': 'INCOMING',
        'claimRewards': 'INCOMING'
    }
}