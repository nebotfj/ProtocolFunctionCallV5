"""TraderJoe Protocol Functions"""

TRADERJOE_FUNCTIONS = {
    'SWAP': {
        'swapExactTokensForTokens': 'BOTH',
        'swapTokensForExactTokens': 'BOTH',
        'swapExactAVAXForTokens': 'OUTGOING',
        'swapTokensForExactAVAX': 'BOTH'
    },
    'LIQUIDITY': {
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING',
        'addLiquidityAVAX': 'OUTGOING',
        'removeLiquidityAVAX': 'INCOMING'
    },
    'LENDING': {
        'supply': 'OUTGOING',
        'withdraw': 'INCOMING',
        'borrow': 'INCOMING',
        'repay': 'OUTGOING'
    },
    'STAKING': {
        'stake': 'OUTGOING',
        'unstake': 'INCOMING',
        'claimRewards': 'INCOMING',
        'compound': 'OUTGOING'
    }
}