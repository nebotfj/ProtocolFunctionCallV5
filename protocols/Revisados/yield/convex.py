"""Convex Finance Protocol Functions"""

CONVEX_FUNCTIONS = {
    'STAKING': {
        'stake': 'OUTGOING',
        'withdraw': 'INCOMING',
        'getReward': 'INCOMING',
        'stakeAll': 'OUTGOING'
    },
    'REWARDS': {
        'claimRewards': 'INCOMING',
        'claimableRewards': 'NEUTRAL',
        'earmarkRewards': 'OUTGOING'
    },
    'BOOSTER': {
        'deposit': 'OUTGOING',
        'withdraw': 'INCOMING',
        'withdrawAll': 'INCOMING',
        'depositAll': 'OUTGOING'
    },
    'LOCKER': {
        'lock': 'OUTGOING',
        'processExpiredLocks': 'INCOMING',
        'processExpiredLocksWithdraw': 'INCOMING'
    }
}