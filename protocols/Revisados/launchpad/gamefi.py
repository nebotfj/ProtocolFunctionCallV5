"""GameFi Protocol Functions"""

GAMEFI_FUNCTIONS = {
    'IGO': {
        'participate': 'OUTGOING',
        'claim': 'INCOMING',
        'refund': 'INCOMING'
    },
    'STAKING': {
        'stakeGAFI': 'OUTGOING',
        'unstakeGAFI': 'INCOMING',
        'claimRewards': 'INCOMING'
    },
    'POOLS': {
        'createPool': 'OUTGOING',
        'joinPool': 'OUTGOING',
        'leavePool': 'INCOMING'
    }
}