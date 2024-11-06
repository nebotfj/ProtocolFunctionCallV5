"""Railway Protocol Functions"""

RAILWAY_FUNCTIONS = {
    'PRIVACY': {
        'createPool': 'OUTGOING',
        'deposit': 'OUTGOING',
        'withdraw': 'INCOMING',
        'mix': 'BOTH'
    },
    'RELAYER': {
        'submitProof': 'OUTGOING',
        'relayTransaction': 'OUTGOING',
        'claimFees': 'INCOMING'
    }
}