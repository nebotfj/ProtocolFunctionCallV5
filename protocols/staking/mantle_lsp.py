"""Mantle LSP Protocol Functions"""

MANTLE_LSP_FUNCTIONS = {
    'STAKING': {
        'stake': 'OUTGOING',
        'unstake': 'INCOMING',
        'claimRewards': 'INCOMING',
        'restake': 'OUTGOING',
        'withdrawRewards': 'INCOMING'
    },
    'DELEGATION': {
        'delegate': 'OUTGOING',
        'undelegate': 'INCOMING',
        'redelegate': 'BOTH'
    },
    'VALIDATOR': {
        'registerValidator': 'OUTGOING',
        'updateValidator': 'OUTGOING',
        'deactivateValidator': 'OUTGOING'
    }
}