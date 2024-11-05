"""Yearn Protocol Functions"""

YEARN_FUNCTIONS = {
    'VAULT': {
        'deposit': 'OUTGOING',
        'withdraw': 'INCOMING',
        'harvest': 'INCOMING',
        'earn': 'OUTGOING'
    },
    'STRATEGIES': {
        'migrate': 'BOTH',
        'withdrawToVault': 'INCOMING',
        'estimatedTotalAssets': 'BOTH',
        'tend': 'OUTGOING'
    },
    'GOVERNANCE': {
        'propose': 'OUTGOING',
        'vote': 'OUTGOING',
        'queue': 'OUTGOING',
        'execute': 'OUTGOING'
    }
}