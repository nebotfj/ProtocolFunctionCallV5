"""Hundred Finance Protocol Functions"""

HUNDRED_FINANCE_FUNCTIONS = {
    'LENDING': {
        'supply': 'OUTGOING',
        'withdraw': 'INCOMING',
        'borrow': 'INCOMING',
        'repay': 'OUTGOING',
        'liquidate': 'BOTH'
    },
    'MARKETS': {
        'enterMarkets': 'OUTGOING',
        'exitMarket': 'INCOMING',
        'claimHND': 'INCOMING'
    },
    'STAKING': {
        'stakeLPTokens': 'OUTGOING',
        'unstakeLPTokens': 'INCOMING',
        'claimRewards': 'INCOMING',
        'lockHND': 'OUTGOING'
    }
}