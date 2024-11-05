FUNCTION_DOCS = {
    # ... (previous categories remain the same) ...
    
    'ORIGIN': {
        'mint': {
            'description': 'Mints OUSD by depositing supported stablecoins',
            'direction': 'OUTGOING'
        },
        'redeem': {
            'description': 'Redeems OUSD for underlying stablecoins',
            'direction': 'INCOMING'
        },
        'redeemAll': {
            'description': 'Redeems all OUSD holdings for stablecoins',
            'direction': 'INCOMING'
        },
        'depositYield': {
            'description': 'Deposits yield from strategies into the vault',
            'direction': 'OUTGOING'
        },
        'claimYield': {
            'description': 'Claims accumulated yield rewards',
            'direction': 'INCOMING'
        },
        'rebase': {
            'description': 'Updates OUSD supply based on yield earned',
            'direction': 'NEUTRAL'
        },
        'createListing': {
            'description': 'Creates NFT listing in Origin marketplace',
            'direction': 'OUTGOING'
        },
        'createOffer': {
            'description': 'Makes an offer for an NFT',
            'direction': 'OUTGOING'
        },
        'acceptOffer': {
            'description': 'Accepts an existing offer for an NFT',
            'direction': 'BOTH'
        },
        'buyNFT': {
            'description': 'Directly purchases an NFT listing',
            'direction': 'OUTGOING'
        },
        'participate': {
            'description': 'Participates in an Origin launchpad sale',
            'direction': 'OUTGOING'
        },
        'registerIP': {
            'description': 'Registers intellectual property in Story Protocol',
            'direction': 'OUTGOING'
        },
        'licenseTo': {
            'description': 'Grants IP license to another address',
            'direction': 'NEUTRAL'
        },
        'collectRoyalties': {
            'description': 'Collects earned IP royalties',
            'direction': 'INCOMING'
        }
    }
}