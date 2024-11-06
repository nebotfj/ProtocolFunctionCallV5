"""ICO/IDO Platform Functions"""

LAUNCHPAD_FUNCTIONS = {
    'COINLIST': {
        'participate': 'OUTGOING',
        'claim': 'INCOMING',
        'register': 'OUTGOING',
        'withdraw': 'INCOMING'
    },
    'POLKASTARTER': {
        'whitelist': 'OUTGOING',
        'participate': 'OUTGOING',
        'claim': 'INCOMING',
        'emergencyWithdraw': 'INCOMING'
    },
    'DAO_MAKER': {
        'registerSHO': 'OUTGOING',
        'participate': 'OUTGOING',
        'claim': 'INCOMING',
        'stake': 'OUTGOING'
    },
    'COPPER_LAUNCH': {
        'createAuction': 'OUTGOING',
        'placeBid': 'OUTGOING',
        'claim': 'INCOMING',
        'withdrawUnsuccessful': 'INCOMING'
    },
    'PINKSALE': {
        'createPresale': 'OUTGOING',
        'participate': 'OUTGOING',
        'claim': 'INCOMING',
        'finalize': 'OUTGOING',
        'cancelPool': 'BOTH'
    },
    'SEEDIFY': {
        'stake': 'OUTGOING',
        'participate': 'OUTGOING',
        'claim': 'INCOMING',
        'unstake': 'INCOMING'
    }
}