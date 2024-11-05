"""Loopring Protocol Functions"""

LOOPRING_FUNCTIONS = {
    'TRADING': {
        'submitOrder': 'OUTGOING',
        'cancelOrder': 'OUTGOING',
        'orderbook': 'NEUTRAL',
        'swap': 'BOTH'
    },
    'LIQUIDITY': {
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING',
        'joinAMM': 'OUTGOING',
        'exitAMM': 'INCOMING'
    },
    'L2_OPERATIONS': {
        'deposit': 'OUTGOING',
        'withdraw': 'INCOMING',
        'transfer': 'BOTH',
        'forceWithdraw': 'OUTGOING'
    },
    'STAKING': {
        'stakeLRC': 'OUTGOING',
        'unstakeLRC': 'INCOMING',
        'claimRewards': 'INCOMING'
    }
}