"""Farcaster Protocol Functions"""

FARCASTER_FUNCTIONS = {
    'SOCIAL': {
        'cast': 'OUTGOING',
        'recast': 'OUTGOING',
        'reply': 'OUTGOING',
        'like': 'OUTGOING'
    },
    'PROFILE': {
        'register': 'OUTGOING',
        'updateProfile': 'OUTGOING',
        'follow': 'OUTGOING',
        'unfollow': 'OUTGOING'
    },
    'STORAGE': {
        'addStorage': 'OUTGOING',
        'removeStorage': 'OUTGOING'
    }
}