"""Granary Finance Protocol Functions"""

GRANARY_FUNCTIONS = {
    'LENDING': {
        'supply': 'OUTGOING',
        'withdraw': 'INCOMING',
        'borrow': 'INCOMING',
        'repay': 'OUTGOING',
        'liquidate': 'BOTH'
    },
    'STAKING': {
        'stakeGRAIN': 'OUTGOING',
        'unstakeGRAIN': 'INCOMING',
        'claimRewards': 'INCOMING'
    },
    'GOVERNANCE': {
        'propose': 'OUTGOING',
        'vote': 'OUTGOING',
        'execute': 'OUTGOING'
    }
}