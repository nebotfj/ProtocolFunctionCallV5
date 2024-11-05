"""Pegaxy Protocol Functions"""

PEGAXY_FUNCTIONS = {
    'RACING': {
        'startRace': 'OUTGOING',
        'claimVIS': 'INCOMING',
        'breedPega': 'OUTGOING',
        'rentPega': 'BOTH'
    },
    'MARKETPLACE': {
        'listPega': 'OUTGOING',
        'buyPega': 'OUTGOING',
        'cancelListing': 'OUTGOING',
        'acceptOffer': 'BOTH'
    },
    'STAKING': {
        'stakePGX': 'OUTGOING',
        'unstakePGX': 'INCOMING',
        'claimRewards': 'INCOMING'
    }
}