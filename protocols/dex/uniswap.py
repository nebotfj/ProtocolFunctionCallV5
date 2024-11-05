"""Uniswap Protocol Functions for all versions"""

UNISWAP_V2_FUNCTIONS = {
    'SWAP': {
        'swapExactTokensForTokens': 'BOTH',
        'swapTokensForExactTokens': 'BOTH',
        'swapExactETHForTokens': 'OUTGOING',
        'swapTokensForExactETH': 'BOTH',
        'swapExactTokensForETH': 'BOTH',
        'swapETHForExactTokens': 'OUTGOING'
    },
    'LIQUIDITY': {
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING',
        'addLiquidityETH': 'OUTGOING',
        'removeLiquidityETH': 'INCOMING',
        'removeLiquidityWithPermit': 'INCOMING',
        'removeLiquidityETHWithPermit': 'INCOMING'
    },
    'FLASH': {
        'flash': 'BOTH'
    }
}

UNISWAP_V3_FUNCTIONS = {
    'SWAP': {
        'exactInput': 'BOTH',
        'exactOutput': 'BOTH',
        'exactInputSingle': 'BOTH',
        'exactOutputSingle': 'BOTH',
        'swap': 'BOTH'
    },
    'LIQUIDITY': {
        'increaseLiquidity': 'OUTGOING',
        'decreaseLiquidity': 'INCOMING',
        'collect': 'INCOMING',
        'createAndInitializePoolIfNecessary': 'OUTGOING',
        'mint': 'OUTGOING',
        'burn': 'INCOMING'
    },
    'POSITION': {
        'positions': 'NEUTRAL',
        'positions_by_ids': 'NEUTRAL',
        'collect_fees': 'INCOMING',
        'transfer': 'BOTH',
        'approve': 'OUTGOING'
    },
    'FLASH': {
        'flash': 'BOTH',
        'flashCallback': 'BOTH'
    },
    'ORACLE': {
        'observe': 'NEUTRAL',
        'increaseObservationCardinalityNext': 'OUTGOING'
    }
}

UNISWAP_V4_FUNCTIONS = {
    'SWAP': {
        'swap': 'BOTH',
        'swapWithHooks': 'BOTH',
        'swapWithPermit': 'BOTH'
    },
    'LIQUIDITY': {
        'modifyPosition': 'BOTH',
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING',
        'donate': 'OUTGOING'
    },
    'HOOKS': {
        'beforeInitialize': 'OUTGOING',
        'afterInitialize': 'OUTGOING',
        'beforeModifyPosition': 'OUTGOING',
        'afterModifyPosition': 'OUTGOING',
        'beforeSwap': 'OUTGOING',
        'afterSwap': 'OUTGOING'
    },
    'FLASH': {
        'flash': 'BOTH',
        'lockAcquired': 'BOTH'
    },
    'POOLS': {
        'initialize': 'OUTGOING',
        'getPool': 'NEUTRAL',
        'setHookFees': 'OUTGOING'
    }
}

# Combined functions for all versions
UNISWAP_FUNCTIONS = {
    'V2': UNISWAP_V2_FUNCTIONS,
    'V3': UNISWAP_V3_FUNCTIONS,
    'V4': UNISWAP_V4_FUNCTIONS
}