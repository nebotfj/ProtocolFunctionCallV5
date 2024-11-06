"""Geist Finance Protocol Functions"""

GEIST_FUNCTIONS = {
    'LENDING': {
        'supply': 'OUTGOING',
        'withdraw': 'INCOMING',
        'borrow': 'INCOMING',
        'repay': 'OUTGOING',
        'liquidate': 'BOTH'
    },
    'STAKING': {
        'stakeGEIST': 'OUTGOING',
        'unstakeGEIST': 'INCOMING',
        'stakeLPTokens': 'OUTGOING',
        'unstakeLPTokens': 'INCOMING',
        'claimRewards': 'INCOMING'
    },
    'VESTING': {
        'lock': 'OUTGOING',
        'unlock': 'INCOMING',
        'claim': 'INCOMING'
    }
}