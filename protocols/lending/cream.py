"""Cream Finance Protocol Functions"""

CREAM_FUNCTIONS = {
    'LENDING': {
        'mint': 'OUTGOING',
        'redeem': 'INCOMING',
        'borrow': 'INCOMING',
        'repay': 'OUTGOING',
        'liquidate': 'BOTH'
    },
    'MARKETS': {
        'enterMarkets': 'OUTGOING',
        'exitMarket': 'INCOMING',
        'getAccountLiquidity': 'NEUTRAL'
    },
    'GOVERNANCE': {
        'propose': 'OUTGOING',
        'castVote': 'OUTGOING',
        'execute': 'OUTGOING',
        'queue': 'OUTGOING'
    }
}