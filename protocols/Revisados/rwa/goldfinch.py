"""Goldfinch Protocol Functions"""

GOLDFINCH_FUNCTIONS = {
    'LENDING': {
        'createLoan': 'OUTGOING',
        'fundLoan': 'OUTGOING',
        'repayLoan': 'OUTGOING',
        'claimRepayment': 'INCOMING'
    },
    'POOLS': {
        'deposit': 'OUTGOING',
        'withdraw': 'INCOMING',
        'stake': 'OUTGOING',
        'unstake': 'INCOMING'
    },
    'MEMBERSHIP': {
        'verifyKYC': 'OUTGOING',
        'mintMembership': 'OUTGOING',
        'updateStatus': 'OUTGOING'
    }
}