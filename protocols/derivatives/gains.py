"""Gains Network Protocol Functions"""

GAINS_FUNCTIONS = {
    'TRADING': {
        'openPosition': 'OUTGOING',
        'closePosition': 'INCOMING',
        'addToPosition': 'OUTGOING',
        'partialClosePosition': 'INCOMING',
        'liquidatePosition': 'BOTH'
    },
    'STAKING': {
        'stakeGNS': 'OUTGOING',
        'unstakeGNS': 'INCOMING',
        'claimRewards': 'INCOMING',
        'compoundRewards': 'OUTGOING'
    },
    'VAULT': {
        'deposit': 'OUTGOING',
        'withdraw': 'INCOMING',
        'rebalanceVault': 'BOTH'
    }
}