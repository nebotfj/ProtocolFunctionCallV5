"""TrueFi Protocol Functions"""

TRUEFI_FUNCTIONS = {
    'LENDING': {
        'createLoan': 'OUTGOING',
        'approveLoan': 'OUTGOING',
        'repayLoan': 'OUTGOING',
        'liquidateLoan': 'BOTH'
    },
    'STAKING': {
        'stakeTRU': 'OUTGOING',
        'unstakeTRU': 'INCOMING',
        'claimRewards': 'INCOMING'
    },
    'PORTFOLIO': {
        'createPortfolio': 'OUTGOING',
        'invest': 'OUTGOING',
        'redeem': 'INCOMING',
        'harvest': 'INCOMING'
    }
}