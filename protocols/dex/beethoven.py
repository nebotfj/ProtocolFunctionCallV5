"""Beethoven X Protocol Functions"""

BEETHOVEN_FUNCTIONS = {
    'TRADING': {
        'swap': 'BOTH',
        'batchSwap': 'BOTH',
        'smartSwap': 'BOTH',
        'flashSwap': 'BOTH'
    },
    'LIQUIDITY': {
        'joinPool': 'OUTGOING',
        'exitPool': 'INCOMING',
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING'
    },
    'STAKING': {
        'stake': 'OUTGOING',
        'unstake': 'INCOMING',
        'getReward': 'INCOMING',
        'compound': 'OUTGOING'
    },
    'GAUGE': {
        'depositLP': 'OUTGOING',
        'withdrawLP': 'INCOMING',
        'claimBeets': 'INCOMING',
        'boostStake': 'OUTGOING'
    }
}