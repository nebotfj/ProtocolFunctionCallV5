"""Unslashed Protocol Functions"""

UNSLASHED_FUNCTIONS = {
    'COVERAGE': {
        'purchasePolicy': 'OUTGOING',
        'fileClaim': 'OUTGOING',
        'withdrawClaim': 'INCOMING',
        'cancelPolicy': 'OUTGOING'
    },
    'CAPITAL': {
        'depositCapital': 'OUTGOING',
        'withdrawCapital': 'INCOMING',
        'claimRewards': 'INCOMING'
    },
    'GOVERNANCE': {
        'propose': 'OUTGOING',
        'vote': 'OUTGOING',
        'execute': 'OUTGOING'
    }
}