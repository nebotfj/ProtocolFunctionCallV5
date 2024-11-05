"""Pocket Network Protocol Functions"""

POCKET_FUNCTIONS = {
    'NODES': {
        'stakeNode': 'OUTGOING',
        'unstakeNode': 'INCOMING',
        'unjailNode': 'OUTGOING',
        'claimRewards': 'INCOMING'
    },
    'APPS': {
        'stakeApp': 'OUTGOING',
        'unstakeApp': 'INCOMING',
        'createApp': 'OUTGOING'
    },
    'GOVERNANCE': {
        'propose': 'OUTGOING',
        'vote': 'OUTGOING',
        'claim': 'INCOMING'
    }
}