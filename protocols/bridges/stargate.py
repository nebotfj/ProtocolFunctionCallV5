"""Stargate Protocol Functions"""

STARGATE_FUNCTIONS = {
    'BRIDGE': {
        'swap': 'BOTH',
        'sendCredits': 'OUTGOING',
        'redeemLocal': 'INCOMING',
        'redeemRemote': 'INCOMING',
        'instantRedeemLocal': 'INCOMING'
    },
    'LIQUIDITY': {
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING',
        'createPool': 'OUTGOING',
        'setFees': 'OUTGOING'
    },
    'STAKING': {
        'stakeLP': 'OUTGOING',
        'unstakeLP': 'INCOMING',
        'claimRewards': 'INCOMING',
        'compoundRewards': 'OUTGOING'
    }
}