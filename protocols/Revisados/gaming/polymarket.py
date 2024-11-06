"""Polymarket Protocol Functions"""

POLYMARKET_FUNCTIONS = {
    'MARKETS': {
        'createMarket': 'OUTGOING',
        'buyOutcome': 'OUTGOING',
        'sellOutcome': 'INCOMING',
        'claimWinnings': 'INCOMING',
        'resolveMarket': 'OUTGOING'
    },
    'LIQUIDITY': {
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING',
        'claimFees': 'INCOMING'
    },
    'COLLATERAL': {
        'depositCollateral': 'OUTGOING',
        'withdrawCollateral': 'INCOMING',
        'bridgeAssets': 'BOTH'
    }
}