"""BullPerks Protocol Functions"""

BULLPERKS_FUNCTIONS = {
    'DEALS': {
        'participate': 'OUTGOING',
        'claim': 'INCOMING',
        'refund': 'INCOMING'
    },
    'STAKING': {
        'stakeBLP': 'OUTGOING',
        'unstakeBLP': 'INCOMING',
        'claimRewards': 'INCOMING'
    },
    'GOVERNANCE': {
        'vote': 'OUTGOING',
        'propose': 'OUTGOING',
        'execute': 'OUTGOING'
    }
}