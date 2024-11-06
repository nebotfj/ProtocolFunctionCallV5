"""Wombat Exchange Protocol Functions"""

WOMBAT_FUNCTIONS = {
    'TRADING': {
        'swap': 'BOTH',
        'swapExactTokensForTokens': 'BOTH',
        'swapTokensForExactTokens': 'BOTH',
        'quotePotentialSwap': 'NEUTRAL'
    },
    'LIQUIDITY': {
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING',
        'addLiquidityNative': 'OUTGOING',
        'removeLiquidityNative': 'INCOMING'
    },
    'STAKING': {
        'deposit': 'OUTGOING',
        'withdraw': 'INCOMING',
        'harvest': 'INCOMING',
        'compound': 'OUTGOING'
    },
    'REWARDS': {
        'claimRewards': 'INCOMING',
        'boostRewards': 'OUTGOING',
        'lockWOM': 'OUTGOING',
        'unlockWOM': 'INCOMING'
    }
}