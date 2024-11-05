"""SpiritSwap Protocol Functions"""

SPIRITSWAP_FUNCTIONS = {
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
    'INSPIRIT': {
        'lockSpirit': 'OUTGOING',
        'unlockSpirit': 'INCOMING',
        'boostFarms': 'OUTGOING',
        'claimBribes': 'INCOMING'
    }
}