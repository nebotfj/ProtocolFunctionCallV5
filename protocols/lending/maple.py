"""Maple Finance Protocol Functions"""

MAPLE_FUNCTIONS = {
    'LENDING': {
        'deposit': 'OUTGOING',
        'withdraw': 'INCOMING',
        'drawdown': 'INCOMING',
        'repay': 'OUTGOING',
        'refinance': 'BOTH'
    },
    'POOL': {
        'createPool': 'OUTGOING',
        'fundPool': 'OUTGOING',
        'closePool': 'INCOMING',
        'claimFees': 'INCOMING'
    },
    'STAKING': {
        'stake': 'OUTGOING',
        'unstake': 'INCOMING',
        'claimRewards': 'INCOMING'
    }
}