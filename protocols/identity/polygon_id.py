"""Polygon ID Protocol Functions"""

POLYGON_ID_FUNCTIONS = {
    'IDENTITY': {
        'createIdentity': 'OUTGOING',
        'updateIdentity': 'OUTGOING',
        'revokeIdentity': 'OUTGOING',
        'verifyCredential': 'NEUTRAL'
    },
    'CLAIMS': {
        'issueClaim': 'OUTGOING',
        'revokeClaim': 'OUTGOING',
        'verifyClaim': 'NEUTRAL'
    },
    'SCHEMAS': {
        'createSchema': 'OUTGOING',
        'updateSchema': 'OUTGOING',
        'validateSchema': 'NEUTRAL'
    }
}