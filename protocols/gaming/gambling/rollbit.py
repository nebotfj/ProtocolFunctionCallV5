"""Rollbit Protocol Functions"""

ROLLBIT_FUNCTIONS = {
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
    'TRADING': {
        'openPosition': 'OUTGOING',
        'closePosition': 'INCOMING',
        'addMargin': 'OUTGOING',
        'takeProfit': 'INCOMING'
    },
    'STAKING': {
        'stakeRLB': 'OUTGOING',
        'unstakeRLB': 'INCOMING',
        'claimRewards': 'INCOMING',
        'compoundRewards': 'OUTGOING'
    }
}