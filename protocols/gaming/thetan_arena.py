"""Thetan Arena Protocol Functions"""

THETAN_ARENA_FUNCTIONS = {
    'GAMEPLAY': {
        'startBattle': 'OUTGOING',
        'endBattle': 'INCOMING',
        'claimTHC': 'INCOMING',
        'upgradeHero': 'OUTGOING'
    },
    'MARKETPLACE': {
        'listHero': 'OUTGOING',
        'buyHero': 'OUTGOING',
        'rentHero': 'BOTH',
        'cancelListing': 'OUTGOING'
    },
    'STAKING': {
        'stakeTHG': 'OUTGOING',
        'unstakeTHG': 'INCOMING',
        'claimRewards': 'INCOMING'
    }
}