"""Hubble Exchange Protocol Functions"""

HUBBLE_FUNCTIONS = {
    'TRADING': {
        'openPosition': 'OUTGOING',
        'closePosition': 'INCOMING',
        'addMargin': 'OUTGOING',
        'removeMargin': 'INCOMING',
        'liquidatePosition': 'BOTH'
    },
    'CLEARING': {
        'settlePosition': 'BOTH',
        'claimInsurance': 'INCOMING',
        'withdrawCollateral': 'INCOMING'
    },
    'STAKING': {
        'stakeHBL': 'OUTGOING',
        'unstakeHBL': 'INCOMING',
        'claimRewards': 'INCOMING'
    }
}