"""Tellor Protocol Functions"""

TELLOR_FUNCTIONS = {
    'ORACLE': {
        'submitValue': 'OUTGOING',
        'disputeValue': 'OUTGOING',
        'vote': 'OUTGOING',
        'retrieveData': 'NEUTRAL'
    },
    'STAKING': {
        'depositStake': 'OUTGOING',
        'requestStakingWithdraw': 'OUTGOING',
        'withdrawStake': 'INCOMING'
    },
    'REWARDS': {
        'claimTip': 'INCOMING',
        'claimReward': 'INCOMING'
    }
}