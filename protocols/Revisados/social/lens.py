"""Lens Protocol Functions"""

LENS_FUNCTIONS = {
    'PROFILE': {
        'createProfile': 'OUTGOING',
        'setProfileImageURI': 'OUTGOING',
        'follow': 'OUTGOING',
        'unfollow': 'OUTGOING'
    },
    'PUBLICATION': {
        'post': 'OUTGOING',
        'comment': 'OUTGOING',
        'mirror': 'OUTGOING',
        'collect': 'OUTGOING'
    },
    'MONETIZATION': {
        'enableModuleForProfile': 'OUTGOING',
        'disableModuleForProfile': 'OUTGOING',
        'claimRevenue': 'INCOMING'
    }
}