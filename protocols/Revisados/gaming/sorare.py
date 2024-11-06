"""Sorare Protocol Functions"""

SORARE_FUNCTIONS = {
    'GAMEPLAY': {
        'createLineup': 'OUTGOING',
        'enterTournament': 'OUTGOING',
        'claimRewards': 'INCOMING',
        'compositeCards': 'OUTGOING'
    },
    'MARKETPLACE': {
        'listCard': 'OUTGOING',
        'buyCard': 'OUTGOING',
        'makeOffer': 'OUTGOING',
        'acceptOffer': 'BOTH'
    },
    'AUCTIONS': {
        'createAuction': 'OUTGOING',
        'placeBid': 'OUTGOING',
        'claimCard': 'INCOMING',
        'withdrawBid': 'INCOMING'
    },
    'REWARDS': {
        'claimETH': 'INCOMING',
        'claimCards': 'INCOMING',
        'stakeSorare': 'OUTGOING',
        'unstakeSorare': 'INCOMING'
    }
}