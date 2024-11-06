"""Maker Protocol Functions"""

MAKER_FUNCTIONS = {
    'VAULT': {
        'openVault': 'OUTGOING',
        'depositCollateral': 'OUTGOING',
        'withdrawCollateral': 'INCOMING',
        'generateDai': 'INCOMING',
        'payback': 'OUTGOING',
        'lockGem': 'OUTGOING',
        'freeGem': 'INCOMING',
        'draw': 'INCOMING',
        'wipe': 'OUTGOING',
        'wipeAll': 'OUTGOING'
    },
    'LIQUIDATION': {
        'bite': 'BOTH',
        'liquidate': 'BOTH',
        'auctionStart': 'OUTGOING',
        'tend': 'OUTGOING',
        'dent': 'OUTGOING',
        'deal': 'INCOMING'
    },
    'GOVERNANCE': {
        'vote': 'OUTGOING',
        'delegate': 'OUTGOING',
        'lock': 'OUTGOING',
        'free': 'INCOMING',
        'plot': 'OUTGOING',
        'lift': 'OUTGOING',
        'propose': 'OUTGOING',
        'exec': 'OUTGOING'
    }
}