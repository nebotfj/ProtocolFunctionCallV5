"""GameStarter Protocol Functions"""

GAMESTARTER_FUNCTIONS = {
    'IGO': {
        'participate': 'OUTGOING',
        'claim': 'INCOMING',
        'refund': 'INCOMING'
    },
    'STAKING': {
        'stakeGAME': 'OUTGOING',
        'unstakeGAME': 'INCOMING',
        'claimRewards': 'INCOMING'
    },
    'TIERS': {
        'lockTokens': 'OUTGOING',
        'unlockTokens': 'INCOMING',
        'upgradeTier': 'OUTGOING'
    }
}