"""Perpetual Protocol Functions"""

PERPETUAL_FUNCTIONS = {
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
        'claimRewards': 'INCOMING'
    },
    'INSURANCE': {
        'depositInsurance': 'OUTGOING',
        'withdrawInsurance': 'INCOMING',
        'claimInsurance': 'INCOMING'
    }
}