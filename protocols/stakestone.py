"""StakeStone Protocol Functions"""

STAKESTONE_FUNCTIONS = {
    'STAKING': {
        'stake': 'OUTGOING',
        'unstake': 'INCOMING',
        'claimRewards': 'INCOMING',
        'compound': 'OUTGOING',
        'requestWithdrawal': 'OUTGOING',
        'claimWithdrawal': 'INCOMING'
    },
    'GOVERNANCE': {
        'vote': 'OUTGOING',
        'delegate': 'OUTGOING',
        'propose': 'OUTGOING',
        'execute': 'OUTGOING'
    },
    'POOL': {
        'joinPool': 'OUTGOING',
        'exitPool': 'INCOMING',
        'swapPoolTokens': 'BOTH'
    }
}