"""VulpeFi Protocol Functions"""

VULPEFI_FUNCTIONS = {
    'TRADING': {
        'swap': 'BOTH',
        'limitOrder': 'OUTGOING',
        'marketOrder': 'BOTH',
        'batchSwap': 'BOTH'
    },
    'LIQUIDITY': {
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING',
        'stakeLPTokens': 'OUTGOING',
        'unstakeLPTokens': 'INCOMING'
    },
    'YIELD': {
        'deposit': 'OUTGOING',
        'withdraw': 'INCOMING',
        'harvest': 'INCOMING',
        'compound': 'OUTGOING'
    }
}