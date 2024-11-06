"""Big Time Protocol Functions"""

BIG_TIME_FUNCTIONS = {
    'GAMEPLAY': {
        'startMission': 'OUTGOING',
        'completeMission': 'INCOMING',
        'claimRewards': 'INCOMING',
        'upgradeGear': 'OUTGOING'
    },
    'MARKETPLACE': {
        'listItem': 'OUTGOING',
        'buyItem': 'OUTGOING',
        'cancelListing': 'OUTGOING',
        'acceptOffer': 'BOTH'
    },
    'CRAFTING': {
        'craftItem': 'OUTGOING',
        'enhanceItem': 'OUTGOING',
        'salvageItem': 'BOTH'
    }
}