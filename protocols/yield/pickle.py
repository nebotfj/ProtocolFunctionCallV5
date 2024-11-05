"""Pickle Finance Protocol Functions"""

PICKLE_FUNCTIONS = {
    'FARM': {
        'deposit': 'OUTGOING',
        'withdraw': 'INCOMING',
        'harvest': 'INCOMING',
        'stakeLPTokens': 'OUTGOING',
        'unstakeLPTokens': 'INCOMING'
    },
    'GAUGE': {
        'depositAll': 'OUTGOING',
        'withdrawAll': 'INCOMING',
        'getReward': 'INCOMING',
        'exit': 'INCOMING'
    },
    'DILL': {
        'stake': 'OUTGOING',
        'unstake': 'INCOMING',
        'claimRewards': 'INCOMING',
        'lockPICKLE': 'OUTGOING'
    }
}