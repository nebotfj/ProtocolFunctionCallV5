"""DIA Protocol Functions"""

DIA_FUNCTIONS = {
    'ORACLE': {
        'updateValue': 'OUTGOING',
        'getValue': 'NEUTRAL',
        'setBatch': 'OUTGOING',
        'updateMetadata': 'OUTGOING'
    },
    'STAKING': {
        'stakeDIA': 'OUTGOING',
        'unstakeDIA': 'INCOMING',
        'claimRewards': 'INCOMING'
    },
    'GOVERNANCE': {
        'propose': 'OUTGOING',
        'vote': 'OUTGOING',
        'execute': 'OUTGOING'
    }
}