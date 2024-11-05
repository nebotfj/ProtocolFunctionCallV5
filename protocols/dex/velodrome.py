"""Velodrome Protocol Functions"""

VELODROME_FUNCTIONS = {
    'SWAP': {
        'swapExactTokensForTokens': 'BOTH',
        'swapExactETHForTokens': 'OUTGOING',
        'swapTokensForExactTokens': 'BOTH',
        'swapTokensForExactETH': 'BOTH'
    },
    'LIQUIDITY': {
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING',
        'createPool': 'OUTGOING',
        'gauge': 'OUTGOING'
    },
    'STAKING': {
        'stake': 'OUTGOING',
        'unstake': 'INCOMING',
        'getReward': 'INCOMING',
        'vote': 'OUTGOING'
    },
    'BRIBES': {
        'notifyRewardAmount': 'OUTGOING',
        'claimBribes': 'INCOMING',
        'addBribe': 'OUTGOING'
    }
}