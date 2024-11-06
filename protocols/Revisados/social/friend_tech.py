"""Friend.tech Protocol Functions"""

FRIEND_TECH_FUNCTIONS = {
    'TRADING': {
        'buyShares': 'OUTGOING',
        'sellShares': 'INCOMING',
        'getBuyPrice': 'NEUTRAL',
        'getSellPrice': 'NEUTRAL'
    },
    'REWARDS': {
        'claimFees': 'INCOMING',
        'withdrawFees': 'INCOMING'
    },
    'SOCIAL': {
        'createProfile': 'OUTGOING',
        'updateProfile': 'OUTGOING'
    }
}