"""Across Protocol Bridge Functions"""

ACROSS_FUNCTIONS = {
    'BRIDGE': {
        'deposit': 'OUTGOING',
        'fillRelay': 'BOTH',
        'speedUpRelay': 'OUTGOING',
        'claim': 'INCOMING'
    },
    'LIQUIDITY': {
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING',
        'claimFees': 'INCOMING'
    },
    'STAKING': {
        'stake': 'OUTGOING',
        'unstake': 'INCOMING',
        'claimRewards': 'INCOMING'
    }
}