"""ZyberSwap Protocol Functions"""

ZYBERSWAP_FUNCTIONS = {
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
        'stake': 'OUTGOING',
        'unstake': 'INCOMING',
        'getReward': 'INCOMING',
        'compound': 'OUTGOING'
    },
    'ZAPPING': {
        'zapIn': 'OUTGOING',
        'zapOut': 'INCOMING',
        'zapInETH': 'OUTGOING',
        'zapOutETH': 'INCOMING'
    }
}