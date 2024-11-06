"""Dopex Options Protocol Functions"""

DOPEX_FUNCTIONS = {
    'OPTIONS': {
        'purchaseOption': 'OUTGOING',
        'exerciseOption': 'BOTH',
        'sellOption': 'INCOMING',
        'settleOption': 'INCOMING'
    },
    'SSOV': {
        'deposit': 'OUTGOING',
        'withdraw': 'INCOMING',
        'claimRewards': 'INCOMING'
    },
    'STAKING': {
        'stakeDPX': 'OUTGOING',
        'unstakeDPX': 'INCOMING',
        'claimStakingRewards': 'INCOMING'
    }
}