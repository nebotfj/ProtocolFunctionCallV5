"""Uniswap Protocol Functions"""

UNISWAP_FUNCTIONS = {
    'SWAP': {
        'swapExactTokensForTokens': 'BOTH',
        'swapTokensForExactTokens': 'BOTH',
        'swapExactETHForTokens': 'OUTGOING',
        'swapTokensForExactETH': 'BOTH',
        'exactInput': 'BOTH',
        'exactOutput': 'BOTH',
        'swapExactTokensForETH': 'BOTH',
        'swapETHForExactTokens': 'OUTGOING',
        'exactInputSingle': 'BOTH',
        'exactOutputSingle': 'BOTH',
        'swap': 'BOTH'
    },
    'LIQUIDITY': {
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING',
        'addLiquidityETH': 'OUTGOING',
        'removeLiquidityETH': 'INCOMING',
        'increaseLiquidity': 'OUTGOING',
        'decreaseLiquidity': 'INCOMING',
        'removeLiquidityWithPermit': 'INCOMING',
        'removeLiquidityETHWithPermit': 'INCOMING'
    },
    'POSITION': {
        'mint': 'OUTGOING',
        'burn': 'INCOMING',
        'collect': 'INCOMING',
        'flash': 'BOTH',
        'initialize': 'OUTGOING',
        'increaseObservationCardinalityNext': 'OUTGOING'
    }
}