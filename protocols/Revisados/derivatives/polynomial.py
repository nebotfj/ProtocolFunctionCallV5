"""Polynomial Protocol Functions"""

POLYNOMIAL_FUNCTIONS = {
    'TRADING': {
        'openPosition': 'OUTGOING',
        'closePosition': 'INCOMING',
        'modifyPosition': 'BOTH',
        'liquidatePosition': 'BOTH'
    },
    'COLLATERAL': {
        'addCollateral': 'OUTGOING',
        'removeCollateral': 'INCOMING',
        'claimLiquidation': 'INCOMING'
    },
    'STAKING': {
        'stakePOLY': 'OUTGOING',
        'unstakePOLY': 'INCOMING',
        'claimRewards': 'INCOMING'
    }
}