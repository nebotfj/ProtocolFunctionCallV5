"""Crypto Unicorns Protocol Functions"""

CRYPTO_UNICORNS_FUNCTIONS = {
    'GAMEPLAY': {
        'breedUnicorns': 'OUTGOING',
        'startRace': 'OUTGOING',
        'claimRaceRewards': 'INCOMING',
        'upgradeUnicorn': 'OUTGOING'
    },
    'FARMING': {
        'plantSeeds': 'OUTGOING',
        'harvestCrops': 'INCOMING',
        'feedUnicorns': 'OUTGOING',
        'collectResources': 'INCOMING'
    },
    'MARKETPLACE': {
        'listUnicorn': 'OUTGOING',
        'buyUnicorn': 'OUTGOING',
        'cancelListing': 'OUTGOING',
        'acceptOffer': 'BOTH'
    },
    'STAKING': {
        'stakeRBW': 'OUTGOING',
        'unstakeRBW': 'INCOMING',
        'claimRewards': 'INCOMING'
    }
}