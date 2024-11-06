"""Vela Exchange Protocol Functions"""

VELA_FUNCTIONS = {
    'TRADING': {
        'placeOrder': 'OUTGOING',
        'cancelOrder': 'OUTGOING',
        'executeOrder': 'BOTH',
        'updateOrder': 'OUTGOING',
        'claimFunding': 'INCOMING'
    },
    'LIQUIDITY': {
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING',
        'claimFees': 'INCOMING'
    },
    'STAKING': {
        'stakeVELA': 'OUTGOING',
        'unstakeVELA': 'INCOMING',
        'claimRewards': 'INCOMING'
    }
}