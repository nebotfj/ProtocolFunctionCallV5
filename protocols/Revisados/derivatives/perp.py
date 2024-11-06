"""Perpetual Protocol Functions"""

PERP_FUNCTIONS = {
    'TRADING': {
        'openPosition': 'OUTGOING',
        'closePosition': 'INCOMING',
        'modifyPosition': 'BOTH',
        'addMargin': 'OUTGOING',
        'removeMargin': 'INCOMING'
    },
    'STAKING': {
        'stakePERP': 'OUTGOING',
        'unstakePERP': 'INCOMING',
        'claimRewards': 'INCOMING',
        'compoundRewards': 'OUTGOING'
    },
    'INSURANCE': {
        'depositInsurance': 'OUTGOING',
        'withdrawInsurance': 'INCOMING',
        'claimInsurance': 'INCOMING'
    }
}