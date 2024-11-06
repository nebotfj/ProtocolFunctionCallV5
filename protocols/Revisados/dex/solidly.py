"""Solidly Protocol Functions"""

SOLIDLY_FUNCTIONS = {
    'TRADING': {
        'swapExactTokensForTokens': 'BOTH',
        'swapExactETHForTokens': 'OUTGOING',
        'swapExactTokensForETH': 'BOTH'
    },
    'LIQUIDITY': {
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING',
        'mint': 'OUTGOING',
        'burn': 'INCOMING'
    },
    'STAKING': {
        'stake': 'OUTGOING',
        'unstake': 'INCOMING',
        'getReward': 'INCOMING',
        'compoundReward': 'OUTGOING'
    },
    'VOTING': {
        'vote': 'OUTGOING',
        'reset': 'OUTGOING',
        'poke': 'OUTGOING'
    }
}