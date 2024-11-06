"""Mycelium Protocol Functions"""

MYCELIUM_FUNCTIONS = {
    'PERPETUALS': {
        'openPosition': 'OUTGOING',
        'closePosition': 'INCOMING',
        'addToPosition': 'OUTGOING',
        'reducePosition': 'INCOMING',
        'liquidatePosition': 'BOTH'
    },
    'STAKING': {
        'stakeMYC': 'OUTGOING',
        'unstakeMYC': 'INCOMING',
        'claimRewards': 'INCOMING',
        'compoundRewards': 'OUTGOING'
    },
    'LIQUIDITY': {
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING',
        'claimFees': 'INCOMING'
    }
}