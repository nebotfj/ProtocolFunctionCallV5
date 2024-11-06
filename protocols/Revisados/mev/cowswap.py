"""CoW Swap Protocol Functions"""

COWSWAP_FUNCTIONS = {
    'TRADING': {
        'placeOrder': 'OUTGOING',
        'cancelOrder': 'OUTGOING',
        'settleOrder': 'BOTH',
        'batchTrade': 'BOTH'
    },
    'SURPLUS': {
        'claimTraderSurplus': 'INCOMING',
        'claimSolverSurplus': 'INCOMING'
    }
}