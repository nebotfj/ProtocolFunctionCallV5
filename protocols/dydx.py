"""dYdX Protocol Functions"""

DYDX_FUNCTIONS = {
    'PERPETUALS': {
        'openPosition': 'OUTGOING',
        'closePosition': 'INCOMING',
        'modifyPosition': 'BOTH',
        'liquidatePosition': 'BOTH',
        'withdrawPnl': 'INCOMING'
    },
    'MARGIN': {
        'deposit': 'OUTGOING',
        'withdraw': 'INCOMING',
        'borrow': 'INCOMING',
        'repay': 'OUTGOING',
        'liquidate': 'BOTH'
    },
    'ORDERS': {
        'placeOrder': 'OUTGOING',
        'cancelOrder': 'OUTGOING',
        'fillOrder': 'BOTH',
        'placeStopOrder': 'OUTGOING',
        'placeTakeProfitOrder': 'OUTGOING'
    },
    'STAKING': {
        'stakeDYDX': 'OUTGOING',
        'unstakeDYDX': 'INCOMING',
        'claimRewards': 'INCOMING',
        'delegateStake': 'OUTGOING'
    },
    'GOVERNANCE': {
        'propose': 'OUTGOING',
        'vote': 'OUTGOING',
        'delegate': 'OUTGOING',
        'execute': 'OUTGOING'
    }
}