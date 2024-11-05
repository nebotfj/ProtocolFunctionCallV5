"""Kwenta Protocol Functions"""

KWENTA_FUNCTIONS = {
    'TRADING': {
        'openPosition': 'OUTGOING',
        'closePosition': 'INCOMING',
        'modifyPosition': 'BOTH',
        'submitOrder': 'OUTGOING',
        'cancelOrder': 'OUTGOING'
    },
    'STAKING': {
        'stakeKWENTA': 'OUTGOING',
        'unstakeKWENTA': 'INCOMING',
        'claimRewards': 'INCOMING',
        'vestRewards': 'OUTGOING'
    },
    'REWARDS': {
        'claimTrading': 'INCOMING',
        'claimStaking': 'INCOMING',
        'compoundRewards': 'OUTGOING'
    }
}