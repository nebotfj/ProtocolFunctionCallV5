"""Gnosis Protocol Functions"""

GNOSIS_FUNCTIONS = {
    'TRADING': {
        'placeOrder': 'OUTGOING',
        'cancelOrder': 'OUTGOING',
        'fulfillOrder': 'BOTH',
        'batchTrade': 'BOTH',
        'settleOrders': 'BOTH'
    },
    'AUCTIONS': {
        'initiateAuction': 'OUTGOING',
        'placeBid': 'OUTGOING',
        'claimAuction': 'INCOMING',
        'cancelAuction': 'OUTGOING'
    },
    'SAFE': {
        'createSafe': 'OUTGOING',
        'executeTransaction': 'OUTGOING',
        'addOwner': 'OUTGOING',
        'removeOwner': 'OUTGOING',
        'replaceOwner': 'OUTGOING',
        'changeThreshold': 'OUTGOING'
    },
    'CONDITIONAL_TOKENS': {
        'splitPosition': 'OUTGOING',
        'mergePositions': 'INCOMING',
        'redeemPositions': 'INCOMING',
        'reportPayouts': 'OUTGOING'
    },
    'GOVERNANCE': {
        'propose': 'OUTGOING',
        'vote': 'OUTGOING',
        'execute': 'OUTGOING',
        'delegate': 'OUTGOING'
    }
}