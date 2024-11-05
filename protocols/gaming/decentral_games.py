"""Decentral Games Protocol Functions"""

DECENTRAL_GAMES_FUNCTIONS = {
    'CASINO': {
        'placeBet': 'OUTGOING',
        'claimWinnings': 'INCOMING',
        'buyChips': 'OUTGOING',
        'sellChips': 'INCOMING',
        'joinTable': 'OUTGOING',
        'leaveTable': 'INCOMING'
    },
    'POKER': {
        'startGame': 'OUTGOING',
        'placeBet': 'OUTGOING',
        'fold': 'OUTGOING',
        'call': 'OUTGOING',
        'raise': 'OUTGOING',
        'showHand': 'NEUTRAL'
    },
    'STAKING': {
        'stakeICE': 'OUTGOING',
        'unstakeICE': 'INCOMING',
        'claimRewards': 'INCOMING',
        'compoundRewards': 'OUTGOING'
    },
    'GOVERNANCE': {
        'propose': 'OUTGOING',
        'vote': 'OUTGOING',
        'execute': 'OUTGOING'
    }
}