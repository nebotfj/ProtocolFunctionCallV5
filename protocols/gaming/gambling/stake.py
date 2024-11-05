"""Stake.com Protocol Functions"""

STAKE_FUNCTIONS = {
    'CASINO': {
        'placeBet': 'OUTGOING',
        'claimWinnings': 'INCOMING',
        'buyCredits': 'OUTGOING',
        'withdrawCredits': 'INCOMING'
    },
    'SPORTS': {
        'placeSportsBet': 'OUTGOING',
        'cashoutBet': 'INCOMING',
        'claimWinnings': 'INCOMING'
    },
    'STAKING': {
        'stakeToken': 'OUTGOING',
        'unstakeToken': 'INCOMING',
        'claimRewards': 'INCOMING'
    }
}