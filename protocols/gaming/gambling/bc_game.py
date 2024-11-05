"""BC.Game Protocol Functions"""

BC_GAME_FUNCTIONS = {
    'CASINO': {
        'spin': 'OUTGOING',
        'placeBet': 'OUTGOING',
        'claimWinnings': 'INCOMING',
        'buyCredits': 'OUTGOING'
    },
    'SPORTS': {
        'placeSportsBet': 'OUTGOING',
        'cashoutBet': 'INCOMING',
        'claimWinnings': 'INCOMING'
    },
    'STAKING': {
        'stakeBCD': 'OUTGOING',
        'unstakeBCD': 'INCOMING',
        'claimRewards': 'INCOMING'
    }
}