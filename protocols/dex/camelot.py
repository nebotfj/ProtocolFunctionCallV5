"""Camelot Protocol Functions"""

CAMELOT_FUNCTIONS = {
    'TRADING': {
        'swapExactTokensForTokens': 'BOTH',
        'swapTokensForExactTokens': 'BOTH',
        'swapExactETHForTokens': 'OUTGOING',
        'swapTokensForExactETH': 'BOTH'
    },
    'LIQUIDITY': {
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING',
        'addLiquidityETH': 'OUTGOING',
        'removeLiquidityETH': 'INCOMING'
    },
    'STAKING': {
        'stake': 'OUTGOING',
        'unstake': 'INCOMING',
        'harvest': 'INCOMING',
        'compound': 'OUTGOING'
    },
    'NFT': {
        'mintPosition': 'OUTGOING',
        'burnPosition': 'INCOMING',
        'modifyPosition': 'BOTH',
        'transferPosition': 'BOTH'
    }
}