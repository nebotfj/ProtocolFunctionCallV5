"""Ribbon Finance Protocol Functions"""

RIBBON_FUNCTIONS = {
    'VAULT': {
        'deposit': 'OUTGOING',
        'withdraw': 'INCOMING',
        'initiateWithdraw': 'OUTGOING',
        'completeWithdraw': 'INCOMING'
    },
    'OPTIONS': {
        'purchaseOption': 'OUTGOING',
        'exerciseOption': 'BOTH',
        'settleOption': 'INCOMING'
    },
    'STAKING': {
        'stakeRBN': 'OUTGOING',
        'unstakeRBN': 'INCOMING',
        'claimRewards': 'INCOMING'
    }
}