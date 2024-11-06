"""Zerion Protocol Functions"""

ZERION_FUNCTIONS = {
    'TRADING': {
        'swap': 'BOTH',
        'multiSwap': 'BOTH',
        'limitOrder': 'OUTGOING',
        'batchSwap': 'BOTH'
    },
    'LIQUIDITY': {
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING',
        'zapIn': 'OUTGOING',
        'zapOut': 'INCOMING'
    },
    'PORTFOLIO': {
        'track': 'NEUTRAL',
        'analyze': 'NEUTRAL',
        'optimize': 'NEUTRAL'
    }
}