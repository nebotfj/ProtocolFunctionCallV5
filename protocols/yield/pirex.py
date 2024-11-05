"""Pirex Protocol Functions"""

PIREX_FUNCTIONS = {
    'STAKING': {
        'deposit': 'OUTGOING',
        'withdraw': 'INCOMING',
        'claimRewards': 'INCOMING',
        'reinvest': 'OUTGOING'
    },
    'AUTOCOMPOUNDING': {
        'compound': 'OUTGOING',
        'harvestRewards': 'INCOMING',
        'distributeYield': 'OUTGOING'
    },
    'GOVERNANCE': {
        'vote': 'OUTGOING',
        'propose': 'OUTGOING',
        'execute': 'OUTGOING'
    }
}