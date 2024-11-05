"""Restaking Protocol Functions"""

RESTAKING_FUNCTIONS = {
    'EIGENLAYER': {
        'deposit': 'OUTGOING',
        'withdraw': 'INCOMING',
        'restake': 'OUTGOING',
        'unstake': 'INCOMING',
        'registerOperator': 'OUTGOING',
        'createPod': 'OUTGOING',
        'delegateToOperator': 'OUTGOING',
        'claimRewards': 'INCOMING'
    }
}