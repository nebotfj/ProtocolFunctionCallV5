"""Yearn V3 Protocol Functions"""

YEARN_V3_FUNCTIONS = {
    'VAULT': {
        'deposit': 'OUTGOING',
        'withdraw': 'INCOMING',
        'harvest': 'INCOMING',
        'migrate': 'BOTH'
    },
    'STRATEGIES': {
        'addStrategy': 'OUTGOING',
        'removeStrategy': 'OUTGOING',
        'updateStrategyDebtRatio': 'OUTGOING',
        'migrateStrategy': 'BOTH'
    },
    'REWARDS': {
        'claimRewards': 'INCOMING',
        'gaugeDeposit': 'OUTGOING',
        'gaugeWithdraw': 'INCOMING'
    }
}