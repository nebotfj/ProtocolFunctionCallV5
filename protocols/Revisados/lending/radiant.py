"""Radiant Capital Protocol Functions"""

RADIANT_FUNCTIONS = {
    'LENDING': {
        'supply': 'OUTGOING',
        'borrow': 'INCOMING',
        'repay': 'OUTGOING',
        'withdraw': 'INCOMING',
        'liquidate': 'BOTH'
    },
    'STAKING': {
        'stakeRDNT': 'OUTGOING',
        'unstakeRDNT': 'INCOMING',
        'claimRewards': 'INCOMING',
        'lockRDNT': 'OUTGOING'
    },
    'GOVERNANCE': {
        'propose': 'OUTGOING',
        'vote': 'OUTGOING',
        'execute': 'OUTGOING'
    }
}