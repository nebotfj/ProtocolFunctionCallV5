"""Symbiosis Protocol Functions"""

SYMBIOSIS_FUNCTIONS = {
    'BRIDGE': {
        'swap': 'BOTH',
        'bridge': 'OUTGOING',
        'claim': 'INCOMING',
        'revert': 'INCOMING'
    },
    'LIQUIDITY': {
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING',
        'stakeLPTokens': 'OUTGOING',
        'unstakeLPTokens': 'INCOMING'
    },
    'REWARDS': {
        'claimRewards': 'INCOMING',
        'compoundRewards': 'OUTGOING',
        'harvestFees': 'INCOMING'
    }
}