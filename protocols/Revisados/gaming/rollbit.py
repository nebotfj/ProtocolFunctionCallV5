"""Rollbit Protocol Functions"""

ROLLBIT_FUNCTIONS = {
    'CASINO': {
        'spin': 'OUTGOING',
        'placeBet': 'OUTGOING',
        'claimWinnings': 'INCOMING',
        'buyCredits': 'OUTGOING',
        'withdrawCredits': 'INCOMING'
    },
    'TRADING': {
        'openPosition': 'OUTGOING',
        'closePosition': 'INCOMING',
        'addMargin': 'OUTGOING',
        'removeMargin': 'INCOMING'
    },
    'STAKING': {
        'stakeRLB': 'OUTGOING',
        'unstakeRLB': 'INCOMING',
        'claimRewards': 'INCOMING'
    }
}