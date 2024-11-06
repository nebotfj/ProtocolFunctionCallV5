"""ZED RUN Protocol Functions"""

ZED_RUN_FUNCTIONS = {
    'RACING': {
        'enterRace': 'OUTGOING',
        'claimPrize': 'INCOMING',
        'breedHorses': 'OUTGOING',
        'sellHorse': 'INCOMING'
    },
    'STAKING': {
        'stakeWETH': 'OUTGOING',
        'unstakeWETH': 'INCOMING',
        'claimRewards': 'INCOMING'
    },
    'TOURNAMENTS': {
        'registerTournament': 'OUTGOING',
        'claimTournamentRewards': 'INCOMING',
        'withdrawEntry': 'INCOMING'
    }
}