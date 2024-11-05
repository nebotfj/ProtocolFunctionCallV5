"""Swell Protocol Functions"""

SWELL_FUNCTIONS = {
    'STAKING': {
        'stake': 'OUTGOING',
        'unstake': 'INCOMING',
        'claimRewards': 'INCOMING',
        'compound': 'OUTGOING'
    },
    'VALIDATOR': {
        'registerValidator': 'OUTGOING',
        'updateValidator': 'OUTGOING',
        'exitValidator': 'OUTGOING'
    },
    'GOVERNANCE': {
        'propose': 'OUTGOING',
        'vote': 'OUTGOING',
        'execute': 'OUTGOING'
    }
}