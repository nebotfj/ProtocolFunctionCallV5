"""PancakeSwap Protocol Functions for all versions"""

PANCAKESWAP_V2_FUNCTIONS = {
    'SWAP': {
        'swapExactTokensForTokens': 'BOTH',
        'swapTokensForExactTokens': 'BOTH',
        'swapExactBNBForTokens': 'OUTGOING',
        'swapTokensForExactBNB': 'BOTH'
    },
    'LIQUIDITY': {
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING',
        'addLiquidityBNB': 'OUTGOING',
        'removeLiquidityBNB': 'INCOMING'
    }
}

PANCAKESWAP_V3_FUNCTIONS = {
    'SWAP': {
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
    'POSITION': {
        'createPosition': 'OUTGOING',
        'addToPosition': 'OUTGOING',
        'removeFromPosition': 'INCOMING',
        'collectFees': 'INCOMING'
    }
}

# Combined functions for all versions
PANCAKESWAP_FUNCTIONS = {
    'V2': PANCAKESWAP_V2_FUNCTIONS,
    'V3': PANCAKESWAP_V3_FUNCTIONS,
    'COMMON': {
        'FARMING': {
            'deposit': 'OUTGOING',
            'withdraw': 'INCOMING',
            'harvest': 'INCOMING',
            'emergencyWithdraw': 'INCOMING'
        },
        'STAKING': {
            'stakeCAKE': 'OUTGOING',
            'unstakeCAKE': 'INCOMING',
            'harvestRewards': 'INCOMING'
        }
    }
}