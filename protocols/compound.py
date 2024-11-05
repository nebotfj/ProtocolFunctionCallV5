"""Compound Protocol Functions"""

COMPOUND_FUNCTIONS = {
    'LENDING': {
        'mint': 'OUTGOING',
        'redeem': 'INCOMING',
        'borrow': 'INCOMING',
        'repayBorrow': 'OUTGOING',
        'liquidateBorrow': 'BOTH'
    },
    'MARKETS': {
        'enterMarkets': 'OUTGOING',
        'exitMarket': 'INCOMING',
        'supply': 'OUTGOING',
        'withdraw': 'INCOMING'
    },
    'GOVERNANCE': {
        'delegate': 'OUTGOING',
        'propose': 'OUTGOING',
        'castVote': 'OUTGOING',
        'queue': 'OUTGOING',
        'execute': 'OUTGOING'
    }
}