"""Betswirl Protocol Functions"""

BETSWIRL_FUNCTIONS = {
    'BETTING': {
        'placeBet': 'OUTGOING',
        'claimWinnings': 'INCOMING',
        'refundBet': 'INCOMING',
        'multibet': 'OUTGOING'
    },
    'STAKING': {
        'stakeBETS': 'OUTGOING',
        'unstakeBETS': 'INCOMING',
        'claimRewards': 'INCOMING',
        'reinvestRewards': 'OUTGOING'
    },
    'BANKROLL': {
        'provideLiquidity': 'OUTGOING',
        'withdrawLiquidity': 'INCOMING',
        'claimBankrollRewards': 'INCOMING'
    }
}