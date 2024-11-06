"""Iron Bank Protocol Functions"""

IRON_BANK_FUNCTIONS = {
    'LENDING': {
        'supply': 'OUTGOING',
        'withdraw': 'INCOMING',
        'borrow': 'INCOMING',
        'repay': 'OUTGOING',
        'liquidate': 'BOTH'
    },
    'MARKETS': {
        'enterMarkets': 'OUTGOING',
        'exitMarket': 'INCOMING',
        'updateInterest': 'NEUTRAL'
    },
    'COLLATERAL': {
        'postCollateral': 'OUTGOING',
        'withdrawCollateral': 'INCOMING',
        'seizeCollateral': 'BOTH'
    }
}