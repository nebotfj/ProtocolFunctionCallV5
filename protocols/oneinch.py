"""1inch Protocol Functions"""

ONEINCH_FUNCTIONS = {
    'SWAP': {
        'swap': 'BOTH',
        'unoswap': 'BOTH',
        'clipperSwap': 'BOTH',
        'fillOrder': 'BOTH',
        'swapWithPermit': 'BOTH'
    },
    'LIMIT_ORDER': {
        'placeLimitOrder': 'OUTGOING',
        'cancelLimitOrder': 'OUTGOING',
        'fillLimitOrder': 'BOTH'
    },
    'AGGREGATION': {
        'discountedSwap': 'BOTH',
        'multiSwap': 'BOTH',
        'megaSwap': 'BOTH'
    },
    'FARMING': {
        'stake': 'OUTGOING',
        'unstake': 'INCOMING',
        'claim': 'INCOMING',
        'exit': 'INCOMING'
    }
}