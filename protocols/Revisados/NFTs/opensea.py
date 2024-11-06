"""OpenSea NFT Marketplace Functions"""

OPENSEA_FUNCTIONS = {
    'LISTING': {
        'createListing': 'OUTGOING',
        'cancelListing': 'OUTGOING',
        'fulfillListing': 'OUTGOING',
        'bulkListing': 'OUTGOING'
    },
    'OFFERS': {
        'createOffer': 'OUTGOING',
        'cancelOffer': 'OUTGOING',
        'fulfillOffer': 'BOTH',
        'bulkOffers': 'OUTGOING'
    },
    'AUCTIONS': {
        'createAuction': 'OUTGOING',
        'placeBid': 'OUTGOING',
        'cancelAuction': 'OUTGOING',
        'endAuction': 'BOTH',
        'claimAuction': 'INCOMING'
    },
    'COLLECTIONS': {
        'setRoyalties': 'OUTGOING',
        'updateCollection': 'OUTGOING',
        'verifyCollection': 'OUTGOING'
    }
}