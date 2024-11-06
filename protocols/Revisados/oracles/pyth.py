"""Pyth Network Functions"""

PYTH_FUNCTIONS = {
    'ORACLE': {
        'updatePrice': 'OUTGOING',
        'getPrice': 'NEUTRAL',
        'getPriceUnsafe': 'NEUTRAL',
        'getEmaPrice': 'NEUTRAL'
    },
    'GOVERNANCE': {
        'proposeUpdate': 'OUTGOING',
        'executeUpdate': 'OUTGOING',
        'claimRewards': 'INCOMING'
    }
}