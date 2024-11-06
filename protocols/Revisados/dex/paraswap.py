"""ParaSwap Protocol Functions"""

PARASWAP_FUNCTIONS = {
    'TRADING': {
        'swap': 'BOTH',
        'multiSwap': 'BOTH',
        'megaSwap': 'BOTH',
        'swapOnUniswap': 'BOTH'
    },
    'LIMIT_ORDERS': {
        'createLimitOrder': 'OUTGOING',
        'cancelLimitOrder': 'OUTGOING',
        'fillLimitOrder': 'BOTH'
    },
    'NFT': {
        'swapNFTs': 'BOTH',
        'wrapNFTs': 'BOTH'
    }
}