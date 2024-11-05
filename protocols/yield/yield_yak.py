"""Yield Yak Protocol Functions"""

YIELD_YAK_FUNCTIONS = {
    'FARMING': {
        'deposit': 'OUTGOING',
        'withdraw': 'INCOMING',
        'harvest': 'INCOMING',
        'reinvest': 'OUTGOING'
    },
    'ROUTER': {
        'findBestPath': 'NEUTRAL',
        'swapNoSplit': 'BOTH',
        'swapMulti': 'BOTH'
    },
    'STAKING': {
        'stakeYAK': 'OUTGOING',
        'unstakeYAK': 'INCOMING',
        'claimRewards': 'INCOMING'
    }
}