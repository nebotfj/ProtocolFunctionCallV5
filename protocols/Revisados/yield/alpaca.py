"""Alpaca Finance Protocol Functions"""

ALPACA_FUNCTIONS = {
    'LENDING': {
        'deposit': 'OUTGOING',
        'withdraw': 'INCOMING',
        'borrow': 'INCOMING',
        'repay': 'OUTGOING'
    },
    'FARMING': {
        'stake': 'OUTGOING',
        'unstake': 'INCOMING',
        'harvest': 'INCOMING',
        'compound': 'OUTGOING'
    },
    'LIQUIDATION': {
        'liquidate': 'BOTH',
        'liquidateMultiple': 'BOTH'
    },
    'GOVERNANCE': {
        'propose': 'OUTGOING',
        'vote': 'OUTGOING',
        'execute': 'OUTGOING'
    }
}