"""Euler Finance Protocol Functions"""

EULER_FUNCTIONS = {
    'LENDING': {
        'deposit': 'OUTGOING',
        'withdraw': 'INCOMING',
        'borrow': 'INCOMING',
        'repay': 'OUTGOING',
        'mint': 'OUTGOING',
        'burn': 'INCOMING'
    },
    'COLLATERAL': {
        'enterMarket': 'OUTGOING',
        'exitMarket': 'INCOMING',
        'transferCollateral': 'BOTH',
        'liquidate': 'BOTH'
    },
    'RISK': {
        'updateRiskParameters': 'OUTGOING',
        'setAssetConfig': 'OUTGOING',
        'setPricingConfig': 'OUTGOING'
    }
}