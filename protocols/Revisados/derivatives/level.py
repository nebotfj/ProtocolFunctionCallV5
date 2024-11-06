"""Level Finance Protocol Functions"""

LEVEL_FUNCTIONS = {
    'TRADING': {
        'openPosition': 'OUTGOING',
        'closePosition': 'INCOMING',
        'increasePosition': 'OUTGOING',
        'decreasePosition': 'INCOMING',
        'liquidatePosition': 'BOTH'
    },
    'LIQUIDITY': {
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING',
        'claimFees': 'INCOMING'
    },
    'STAKING': {
        'stakeLVL': 'OUTGOING',
        'unstakeLVL': 'INCOMING',
        'claimRewards': 'INCOMING',
        'compoundRewards': 'OUTGOING'
    }
}