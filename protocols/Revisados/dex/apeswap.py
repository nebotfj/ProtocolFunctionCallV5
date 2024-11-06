"""ApeSwap Protocol Functions"""

APESWAP_FUNCTIONS = {
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
    'STAKING': {
        'stakeBANANA': 'OUTGOING',
        'unstakeBANANA': 'INCOMING',
        'claimRewards': 'INCOMING'
    }
}