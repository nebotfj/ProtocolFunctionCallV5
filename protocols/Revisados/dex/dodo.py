"""DODO Protocol Functions"""

DODO_FUNCTIONS = {
    'TRADING': {
        'dodoSwap': 'BOTH',
        'externalSwap': 'BOTH',
        'dodoMultiSwap': 'BOTH',
        'routerSwap': 'BOTH'
    },
    'LIQUIDITY': {
        'depositBase': 'OUTGOING',
        'depositQuote': 'OUTGOING',
        'withdrawBase': 'INCOMING',
        'withdrawQuote': 'INCOMING',
        'buyShares': 'OUTGOING',
        'sellShares': 'INCOMING'
    },
    'POOL': {
        'createPool': 'OUTGOING',
        'resetPool': 'OUTGOING',
        'bidPool': 'OUTGOING',
        'askPool': 'OUTGOING',
        'updatePool': 'OUTGOING'
    },
    'VENDING_MACHINE': {
        'createVendingMachine': 'OUTGOING',
        'buyFromVending': 'OUTGOING',
        'sellToVending': 'INCOMING',
        'updateVending': 'OUTGOING'
    }
}