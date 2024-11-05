"""DeFi Kingdoms Protocol Functions"""

DEFI_KINGDOMS_FUNCTIONS = {
    'HEROES': {
        'summonHero': 'OUTGOING',
        'levelUpHero': 'OUTGOING',
        'startQuest': 'OUTGOING',
        'completeQuest': 'INCOMING',
        'claimRewards': 'INCOMING'
    },
    'GARDENS': {
        'plantSeeds': 'OUTGOING',
        'harvestPlants': 'INCOMING',
        'waterPlants': 'OUTGOING',
        'collectRewards': 'INCOMING'
    },
    'MARKETPLACE': {
        'listHero': 'OUTGOING',
        'buyHero': 'OUTGOING',
        'rentHero': 'BOTH',
        'cancelListing': 'OUTGOING'
    },
    'MEDITATION': {
        'startMeditation': 'OUTGOING',
        'completeMeditation': 'INCOMING',
        'claimMeditationRewards': 'INCOMING'
    }
}