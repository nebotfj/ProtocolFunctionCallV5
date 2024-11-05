"""InsurAce Protocol Functions"""

INSURACE_FUNCTIONS = {
    'COVERAGE': {
        'buyCover': 'OUTGOING',
        'renewCover': 'OUTGOING',
        'submitClaim': 'OUTGOING',
        'redeemClaim': 'INCOMING'
    },
    'STAKING': {
        'stakeINSUR': 'OUTGOING',
        'unstakeINSUR': 'INCOMING',
        'claimRewards': 'INCOMING'
    },
    'INVESTMENT': {
        'invest': 'OUTGOING',
        'withdraw': 'INCOMING',
        'reinvest': 'OUTGOING'
    }
}