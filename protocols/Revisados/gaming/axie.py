"""Axie Infinity Protocol Functions"""

AXIE_FUNCTIONS = {
    'GAMEPLAY': {
        'startGame': 'OUTGOING',
        'endGame': 'INCOMING',
        'claimSLP': 'INCOMING',
        'breedAxies': 'OUTGOING'
    },
    'MARKETPLACE': {
        'listAxie': 'OUTGOING',
        'buyAxie': 'OUTGOING',
        'cancelListing': 'OUTGOING',
        'acceptOffer': 'BOTH'
    },
    'LAND': {
        'buyLand': 'OUTGOING',
        'sellLand': 'INCOMING',
        'stakeLand': 'OUTGOING',
        'harvestFromLand': 'INCOMING'
    },
    'STAKING': {
        'stakeAXS': 'OUTGOING',
        'unstakeAXS': 'INCOMING',
        'claimRewards': 'INCOMING',
        'restakeRewards': 'OUTGOING'
    }
}