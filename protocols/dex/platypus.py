"""Platypus Finance Protocol Functions"""

PLATYPUS_FUNCTIONS = {
    'TRADING': {
        'swap': 'BOTH',
        'flashSwap': 'BOTH',
        'multiSwap': 'BOTH'
    },
    'LIQUIDITY': {
        'deposit': 'OUTGOING',
        'withdraw': 'INCOMING',
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING'
    },
    'FARMING': {
        'stake': 'OUTGOING',
        'unstake': 'INCOMING',
        'harvest': 'INCOMING',
        'compound': 'OUTGOING'
    },
    'VESTING': {
        'lock': 'OUTGOING',
        'unlock': 'INCOMING',
        'claim': 'INCOMING'
    }
}