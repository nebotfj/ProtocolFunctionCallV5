"""Duelbits Protocol Functions"""

DUELBITS_FUNCTIONS = {
    'CASINO': {
        'placeBet': 'OUTGOING',
        'playDice': 'OUTGOING',
        'playCrash': 'OUTGOING',
        'playRoulette': 'OUTGOING',
        'claimWinnings': 'INCOMING'
    },
    'SPORTS': {
        'placeSportsBet': 'OUTGOING',
        'createAccumulator': 'OUTGOING',
        'cashoutBet': 'INCOMING',
        'claimWinnings': 'INCOMING'
    },
    'REWARDS': {
        'claimRakeback': 'INCOMING',
        'claimVIPRewards': 'INCOMING',
        'redeemPoints': 'BOTH',
        'claimBonus': 'INCOMING'
    }
}