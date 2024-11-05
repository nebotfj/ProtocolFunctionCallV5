"""KyberSwap Protocol Functions"""

KYBERSWAP_FUNCTIONS = {
    'TRADING': {
        'swapExactTokensForTokens': 'BOTH',
        'swapTokensForExactTokens': 'BOTH',
        'swapExactETHForTokens': 'OUTGOING',
        'swapTokensForExactETH': 'BOTH'
    },
    'LIQUIDITY': {
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING',
        'addStaticLiquidity': 'OUTGOING',
        'removeStaticLiquidity': 'INCOMING'
    },
    'ELASTIC': {
        'mint': 'OUTGOING',
        'burn': 'INCOMING',
        'collect': 'INCOMING',
        'compound': 'OUTGOING'
    },
    'FARMING': {
        'deposit': 'OUTGOING',
        'withdraw': 'INCOMING',
        'harvest': 'INCOMING',
        'emergencyWithdraw': 'INCOMING'
    }
}