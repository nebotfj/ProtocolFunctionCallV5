"""Eden Network Protocol Functions"""

EDEN_FUNCTIONS = {
    'SLOTS': {
        'reserveSlot': 'OUTGOING',
        'cancelReservation': 'OUTGOING',
        'claimSlotRewards': 'INCOMING'
    },
    'STAKING': {
        'stakeEDEN': 'OUTGOING',
        'unstakeEDEN': 'INCOMING',
        'claimStakingRewards': 'INCOMING'
    },
    'BUNDLES': {
        'submitBundle': 'OUTGOING',
        'cancelBundle': 'OUTGOING'
    }
}