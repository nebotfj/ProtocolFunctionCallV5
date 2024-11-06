"""Rarible NFT Marketplace Functions"""

RARIBLE_FUNCTIONS = {
    'TRADING': {
        'sell': 'OUTGOING',
        'buy': 'OUTGOING',
        'cancelOrder': 'OUTGOING',
        'acceptBid': 'BOTH'
    },
    'CREATION': {
        'mint': 'OUTGOING',
        'mintAndSell': 'OUTGOING',
        'burn': 'OUTGOING',
        'mintBatch': 'OUTGOING'
    },
    'LAZY_MINTING': {
        'createLazyMint': 'OUTGOING',
        'fulfillLazyMint': 'BOTH',
        'cancelLazyMint': 'OUTGOING'
    },
    'ROYALTIES': {
        'setRoyalties': 'OUTGOING',
        'updateRoyalties': 'OUTGOING',
        'claimRoyalties': 'INCOMING'
    }
}