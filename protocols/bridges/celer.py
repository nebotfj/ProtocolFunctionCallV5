"""Celer Bridge Protocol Functions"""

CELER_FUNCTIONS = {
    'BRIDGE': {
        'send': 'OUTGOING',
        'relay': 'BOTH',
        'withdraw': 'INCOMING',
        'refund': 'INCOMING'
    },
    'LIQUIDITY': {
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING',
        'claimFees': 'INCOMING'
    },
    'STAKING': {
        'stakeCELR': 'OUTGOING',
        'unstakeCELR': 'INCOMING',
        'claimRewards': 'INCOMING'
    }
}