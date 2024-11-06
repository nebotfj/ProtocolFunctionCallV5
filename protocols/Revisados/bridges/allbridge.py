"""Allbridge Protocol Functions"""

ALLBRIDGE_FUNCTIONS = {
    'BRIDGE': {
        'bridge': 'OUTGOING',
        'swap': 'BOTH',
        'claim': 'INCOMING',
        'bridgeTokens': 'OUTGOING',
        'unwrapTokens': 'INCOMING'
    },
    'LIQUIDITY': {
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING',
        'stakeLPTokens': 'OUTGOING',
        'unstakeLPTokens': 'INCOMING',
        'claimFees': 'INCOMING'
    },
    'FARMING': {
        'stake': 'OUTGOING',
        'unstake': 'INCOMING',
        'harvest': 'INCOMING',
        'compound': 'OUTGOING'
    }
}