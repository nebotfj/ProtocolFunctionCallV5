"""Aztec Protocol Functions"""

AZTEC_FUNCTIONS = {
    'SHIELD': {
        'deposit': 'OUTGOING',
        'withdraw': 'INCOMING',
        'transfer': 'BOTH',
        'shield': 'OUTGOING'
    },
    'DEFI_BRIDGE': {
        'bridgeDeposit': 'OUTGOING',
        'bridgeWithdraw': 'INCOMING',
        'bridgeInteraction': 'BOTH'
    },
    'PROOFS': {
        'generateProof': 'NEUTRAL',
        'verifyProof': 'NEUTRAL',
        'processProof': 'OUTGOING'
    }
}