"""Stader Protocol Functions"""

STADER_FUNCTIONS = {
    'STAKING': {
        'deposit': 'OUTGOING',
        'requestWithdrawal': 'OUTGOING',
        'claimWithdrawal': 'INCOMING',
        'claimRewards': 'INCOMING'
    },
    'VALIDATOR': {
        'registerValidator': 'OUTGOING',
        'exitValidator': 'OUTGOING',
        'claimValidatorRewards': 'INCOMING'
    },
    'PERMISSIONLESS': {
        'createPermissionlessNode': 'OUTGOING',
        'operateNode': 'OUTGOING',
        'claimNodeRewards': 'INCOMING'
    }
}