"""Civic Protocol Functions"""

CIVIC_FUNCTIONS = {
    'IDENTITY': {
        'createIdentity': 'OUTGOING',
        'updateIdentity': 'OUTGOING',
        'deleteIdentity': 'OUTGOING',
        'verifyIdentity': 'NEUTRAL'
    },
    'GATEKEEPER': {
        'registerGatekeeper': 'OUTGOING',
        'verifyGatekeeper': 'NEUTRAL',
        'updateGatekeeper': 'OUTGOING'
    },
    'TOKEN': {
        'stake': 'OUTGOING',
        'unstake': 'INCOMING',
        'claimRewards': 'INCOMING'
    }
}