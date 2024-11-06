"""BrightID Protocol Functions"""

BRIGHTID_FUNCTIONS = {
    'VERIFICATION': {
        'verify': 'OUTGOING',
        'sponsor': 'OUTGOING',
        'link': 'OUTGOING',
        'removeConnection': 'OUTGOING'
    },
    'GROUPS': {
        'createGroup': 'OUTGOING',
        'joinGroup': 'OUTGOING',
        'leaveGroup': 'OUTGOING',
        'inviteMember': 'OUTGOING'
    },
    'CONTEXT': {
        'addContext': 'OUTGOING',
        'removeContext': 'OUTGOING',
        'updateContext': 'OUTGOING'
    }
}