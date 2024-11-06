"""STEPN Protocol Functions"""

STEPN_FUNCTIONS = {
    'GAMEPLAY': {
        'startMove': 'OUTGOING',
        'endMove': 'INCOMING',
        'claimGST': 'INCOMING',
        'levelUpShoe': 'OUTGOING'
    },
    'MARKETPLACE': {
        'listShoe': 'OUTGOING',
        'buyShoe': 'OUTGOING',
        'cancelListing': 'OUTGOING',
        'acceptOffer': 'BOTH'
    },
    'STAKING': {
        'stakeGMT': 'OUTGOING',
        'unstakeGMT': 'INCOMING',
        'claimRewards': 'INCOMING'
    }
}