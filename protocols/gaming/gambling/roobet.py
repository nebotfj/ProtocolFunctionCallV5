"""Roobet Protocol Functions"""

ROOBET_FUNCTIONS = {
    'CASINO': {
        'placeBet': 'OUTGOING',
        'spinSlot': 'OUTGOING',
        'playBlackjack': 'BOTH',
        'playRoulette': 'OUTGOING',
        'claimWinnings': 'INCOMING'
    },
    'SPORTS': {
        'placeSportsBet': 'OUTGOING',
        'cashoutBet': 'INCOMING',
        'createParlay': 'OUTGOING',
        'claimWinnings': 'INCOMING'
    },
    'REWARDS': {
        'claimRakeBack': 'INCOMING',
        'claimVIPBonus': 'INCOMING',
        'redeemPoints': 'BOTH',
        'claimDailyBonus': 'INCOMING'
    }
}