"""Gods Unchained Protocol Functions"""

GODS_UNCHAINED_FUNCTIONS = {
    'GAMEPLAY': {
        'startMatch': 'OUTGOING',
        'endMatch': 'INCOMING',
        'claimRewards': 'INCOMING',
        'forgeCard': 'OUTGOING'
    },
    'MARKETPLACE': {
        'listCard': 'OUTGOING',
        'buyCard': 'OUTGOING',
        'cancelListing': 'OUTGOING',
        'acceptOffer': 'BOTH'
    },
    'STAKING': {
        'stakeGODS': 'OUTGOING',
        'unstakeGODS': 'INCOMING',
        'claimYield': 'INCOMING',
        'compoundRewards': 'OUTGOING'
    },
    'FUSION': {
        'fuseCards': 'OUTGOING',
        'splitCard': 'INCOMING',
        'upgradeCard': 'OUTGOING'
    }
}