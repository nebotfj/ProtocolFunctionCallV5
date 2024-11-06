"""Across V2 Protocol Functions"""

ACROSS_V2_FUNCTIONS = {
    'BRIDGE': {
        'deposit': 'OUTGOING',
        'fillRelay': 'BOTH',
        'speedUpRelay': 'OUTGOING',
        'claim': 'INCOMING'
    },
    'LIQUIDITY': {
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING',
        'claimFees': 'INCOMING',
        'rebalancePool': 'BOTH'
    },
    'REWARDS': {
        'stakeACX': 'OUTGOING',
        'unstakeACX': 'INCOMING',
        'claimRewards': 'INCOMING',
        'compoundRewards': 'OUTGOING'
    }
}