"""Morpho Protocol Functions"""

MORPHO_FUNCTIONS = {
    'LENDING': {
        'supply': 'OUTGOING',
        'withdraw': 'INCOMING',
        'borrow': 'INCOMING',
        'repay': 'OUTGOING',
        'liquidate': 'BOTH'
    },
    'P2P_MATCHING': {
        'matchLenders': 'BOTH',
        'matchBorrowers': 'BOTH',
        'updateIndexes': 'OUTGOING'
    },
    'REWARDS': {
        'claimRewards': 'INCOMING',
        'claimMorpho': 'INCOMING',
        'stakeMorpho': 'OUTGOING'
    }
}