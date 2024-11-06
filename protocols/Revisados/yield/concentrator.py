"""Concentrator Protocol Functions"""

CONCENTRATOR_FUNCTIONS = {
    'VAULT': {
        'deposit': 'OUTGOING',
        'withdraw': 'INCOMING',
        'harvest': 'INCOMING',
        'compound': 'OUTGOING'
    },
    'STRATEGY': {
        'setStrategy': 'OUTGOING',
        'migrateStrategy': 'BOTH',
        'updateStrategyDebtRatio': 'OUTGOING'
    },
    'REWARDS': {
        'getReward': 'INCOMING',
        'notifyRewardAmount': 'OUTGOING',
        'addReward': 'OUTGOING'
    }
}