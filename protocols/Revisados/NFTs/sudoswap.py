"""Sudoswap NFT Marketplace Functions"""

SUDOSWAP_FUNCTIONS = {
    'POOL': {
        'createPool': 'OUTGOING',
        'addNFT': 'OUTGOING',
        'removeNFT': 'INCOMING',
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING'
    },
    'TRADING': {
        'swapNFTForToken': 'BOTH',
        'swapTokenForNFT': 'BOTH',
        'swapNFTForAnyNFT': 'BOTH',
        'robustSwapNFT': 'BOTH'
    },
    'BONDING_CURVE': {
        'updateDelta': 'OUTGOING',
        'updateSpotPrice': 'OUTGOING',
        'updateFee': 'OUTGOING'
    }
}