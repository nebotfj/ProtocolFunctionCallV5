"""Jones DAO Protocol Functions"""

JONES_DAO_FUNCTIONS = {
    'VAULTS': {
        'deposit': 'OUTGOING',
        'withdraw': 'INCOMING',
        'harvest': 'INCOMING',
        'compound': 'OUTGOING'
    },
    'OPTIONS': {
        'buyOption': 'OUTGOING',
        'sellOption': 'INCOMING',
        'exercise': 'BOTH',
        'settle': 'INCOMING'
    },
    'STAKING': {
        'stakeJONES': 'OUTGOING',
        'unstakeJONES': 'INCOMING',
        'claimRewards': 'INCOMING'
    }
}