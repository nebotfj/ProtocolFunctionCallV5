"""Raydium Protocol Functions"""

RAYDIUM_FUNCTIONS = {
    'SWAP': {
        'swap': 'BOTH',
        'routeSwap': 'BOTH',
        'swapBaseIn': 'BOTH',
        'swapBaseOut': 'BOTH'
    },
    'LIQUIDITY': {
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING',
        'createPool': 'OUTGOING',
        'closePool': 'OUTGOING'
    },
    'FARMING': {
        'deposit': 'OUTGOING',
        'withdraw': 'INCOMING',
        'harvest': 'INCOMING',
        'emergencyWithdraw': 'INCOMING'
    },
    'STAKING': {
        'stakeRAY': 'OUTGOING',
        'unstakeRAY': 'INCOMING',
        'claimRewards': 'INCOMING'
    }
}