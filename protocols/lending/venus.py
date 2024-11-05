"""Venus Protocol Functions"""

VENUS_FUNCTIONS = {
    'LENDING': {
        'mint': 'OUTGOING',
        'redeem': 'INCOMING',
        'borrow': 'INCOMING',
        'repay': 'OUTGOING',
        'liquidate': 'BOTH'
    },
    'MARKETS': {
        'enterMarkets': 'OUTGOING',
        'exitMarket': 'INCOMING',
        'updateVenusSupplyIndex': 'OUTGOING',
        'updateVenusBorrowIndex': 'OUTGOING'
    },
    'REWARDS': {
        'claimVenus': 'INCOMING',
        'claimVenusAsCollateral': 'INCOMING',
        'distributeSupplierVenus': 'INCOMING',
        'distributeBorrowerVenus': 'INCOMING'
    }
}