"""LayerZero Protocol Functions"""

LAYERZERO_FUNCTIONS = {
    'BRIDGE': {
        'send': 'OUTGOING',
        'receive': 'INCOMING',
        'quote': 'NEUTRAL',
        'validateTransactionProof': 'NEUTRAL',
        'retryPayload': 'OUTGOING'
    },
    'STAKING': {
        'stakeLPTokens': 'OUTGOING',
        'unstakeLPTokens': 'INCOMING',
        'claimRewards': 'INCOMING',
        'compoundRewards': 'OUTGOING'
    },
    'RELAYER': {
        'assignJob': 'OUTGOING',
        'submitProof': 'OUTGOING',
        'claimFees': 'INCOMING'
    }
}