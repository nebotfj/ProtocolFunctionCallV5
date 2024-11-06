"""LooksRare NFT Marketplace Functions"""

LOOKSRARE_FUNCTIONS = {
    'TRADING': {
        'createOrder': 'OUTGOING',
        'cancelOrder': 'OUTGOING',
        'matchOrder': 'BOTH',
        'matchOrders': 'BOTH'
    },
    'REWARDS': {
        'stakeLOOKS': 'OUTGOING',
        'unstakeLOOKS': 'INCOMING',
        'claimRewards': 'INCOMING',
        'compoundRewards': 'OUTGOING'
    },
    'ROYALTIES': {
        'setRoyalties': 'OUTGOING',
        'updateRoyalties': 'OUTGOING',
        'claimRoyalties': 'INCOMING'
    }
}