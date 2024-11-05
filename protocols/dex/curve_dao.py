"""CurveDAO Protocol Functions"""

CURVE_DAO_FUNCTIONS = {
    'VOTING': {
        'vote': 'OUTGOING',
        'createLock': 'OUTGOING',
        'increaseAmount': 'OUTGOING',
        'increaseUnlockTime': 'OUTGOING',
        'withdraw': 'INCOMING'
    },
    'GAUGE': {
        'gaugeVote': 'OUTGOING',
        'depositGauge': 'OUTGOING',
        'withdrawGauge': 'INCOMING',
        'claimRewards': 'INCOMING'
    },
    'FEE_DISTRIBUTION': {
        'claimFees': 'INCOMING',
        'burnAdmin': 'OUTGOING',
        'commitOwnership': 'OUTGOING',
        'applyOwnership': 'OUTGOING'
    }
}