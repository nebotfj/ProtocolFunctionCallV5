"""Gambit Protocol Functions"""

GAMBIT_FUNCTIONS = {
    'CASINO': {
        'placeBet': 'OUTGOING',
        'playDice': 'OUTGOING',
        'playCrash': 'OUTGOING',
        'playPlinko': 'OUTGOING',
        'claimWinnings': 'INCOMING'
    },
    'SPORTS': {
        'placeSportsBet': 'OUTGOING',
        'createAccumulator': 'OUTGOING',
        'cashoutBet': 'INCOMING',
        'claimWinnings': 'INCOMING'
    },
    'STAKING': {
        'stakeGMBT': 'OUTGOING',
        'unstakeGMBT': 'INCOMING',
        'claimRewards': 'INCOMING',
        'compoundRewards': 'OUTGOING'
    }
}