"""X2Y2 NFT Marketplace Functions"""

X2Y2_FUNCTIONS = {
    'TRADING': {
        'list': 'OUTGOING',
        'buy': 'OUTGOING',
        'cancel': 'OUTGOING',
        'bulkList': 'OUTGOING',
        'bulkBuy': 'OUTGOING'
    },
    'OFFERS': {
        'makeOffer': 'OUTGOING',
        'cancelOffer': 'OUTGOING',
        'acceptOffer': 'BOTH'
    },
    'REWARDS': {
        'stakeX2Y2': 'OUTGOING',
        'unstakeX2Y2': 'INCOMING',
        'claimRewards': 'INCOMING'
    }
}