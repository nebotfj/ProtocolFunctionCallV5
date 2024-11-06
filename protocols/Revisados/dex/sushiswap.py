"""SushiSwap Protocol Functions for all versions"""

SUSHISWAP_V1_FUNCTIONS = {
    'SWAP': {
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
    }
}

SUSHISWAP_V2_FUNCTIONS = {
    'SWAP': {
        'swapExactTokensForTokens': 'BOTH',
        'swapTokensForExactTokens': 'BOTH',
        'swapExactETHForTokens': 'OUTGOING',
        'swapTokensForExactETH': 'BOTH',
        'swapExactTokensForTokensSupportingFeeOnTransferTokens': 'BOTH'
    },
    'LIQUIDITY': {
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING',
        'addLiquidityETH': 'OUTGOING',
        'removeLiquidityETH': 'INCOMING',
        'removeLiquidityWithPermit': 'INCOMING'
    },
    'TRIDENT': {
        'exactInput': 'BOTH',
        'exactOutput': 'BOTH',
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING'
    }
}

SUSHISWAP_V3_FUNCTIONS = {
    'TRADING': {
        'exactInput': 'BOTH',
        'exactOutput': 'BOTH',
        'exactInputSingle': 'BOTH',
        'exactOutputSingle': 'BOTH'
    },
    'LIQUIDITY': {
        'mint': 'OUTGOING',
        'burn': 'INCOMING',
        'collect': 'INCOMING',
        'increaseLiquidity': 'OUTGOING',
        'decreaseLiquidity': 'INCOMING'
    },
    'CONCENTRATED': {
        'createPool': 'OUTGOING',
        'setFeeProtocol': 'OUTGOING',
        'collectProtocol': 'INCOMING'
    }
}

# Combined functions for all versions
SUSHISWAP_FUNCTIONS = {
    'V1': SUSHISWAP_V1_FUNCTIONS,
    'V2': SUSHISWAP_V2_FUNCTIONS,
    'V3': SUSHISWAP_V3_FUNCTIONS,
    'COMMON': {
        'FARMING': {
            'deposit': 'OUTGOING',
            'withdraw': 'INCOMING',
            'harvest': 'INCOMING',
            'emergencyWithdraw': 'INCOMING'
        }
    }
}