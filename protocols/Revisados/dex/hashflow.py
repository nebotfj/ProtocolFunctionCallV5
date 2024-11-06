"""Hashflow DEX Functions"""

HASHFLOW_FUNCTIONS = {
    'TRADING': {
        'requestQuote': 'NEUTRAL',
        'fillQuote': 'BOTH',
        'limitOrder': 'OUTGOING',
        'cancelOrder': 'OUTGOING'
    },
    'RFQ': {
        'requestForQuote': 'NEUTRAL',
        'provideQuote': 'OUTGOING',
        'acceptQuote': 'BOTH'
    },
    'POOLS': {
        'createPool': 'OUTGOING',
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING'
    }
}