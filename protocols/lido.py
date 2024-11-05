"""Lido Staking Protocol Functions"""

LIDO_FUNCTIONS = {
    'STAKING': {
        'submit': 'OUTGOING',
        'requestWithdrawals': 'OUTGOING',
        'claimWithdrawals': 'INCOMING',
        'stake': 'OUTGOING',
        'unstake': 'INCOMING',
        'withdraw': 'INCOMING'
    },
    'REWARDS': {
        'claimRewards': 'INCOMING',
        'distributeRewards': 'INCOMING',
        'claimStakingRewards': 'INCOMING'
    },
    'GOVERNANCE': {
        'vote': 'OUTGOING',
        'delegate': 'OUTGOING',
        'proposeVote': 'OUTGOING',
        'executeVote': 'OUTGOING'
    }
}