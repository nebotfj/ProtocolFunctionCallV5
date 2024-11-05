"""Umbrella Protocol Functions"""

UMBRELLA_FUNCTIONS = {
    'ORACLE': {
        'submitPrice': 'OUTGOING',
        'validatePrice': 'NEUTRAL',
        'disputePrice': 'OUTGOING',
        'resolveDispute': 'BOTH'
    },
    'STAKING': {
        'stakeUMB': 'OUTGOING',
        'unstakeUMB': 'INCOMING',
        'claimRewards': 'INCOMING'
    },
    'REGISTRY': {
        'registerValidator': 'OUTGOING',
        'deregisterValidator': 'OUTGOING',
        'updateRegistry': 'OUTGOING'
    }
}