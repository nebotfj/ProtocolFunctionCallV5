"""Arweave Protocol Functions"""

ARWEAVE_FUNCTIONS = {
    'STORAGE': {
        'uploadData': 'OUTGOING',
        'downloadData': 'INCOMING',
        'createBundle': 'OUTGOING',
        'mintToken': 'OUTGOING'
    },
    'MINING': {
        'submitBlock': 'OUTGOING',
        'verifyBlock': 'NEUTRAL',
        'claimRewards': 'INCOMING'
    },
    'PROFIT_SHARING': {
        'createCommunity': 'OUTGOING',
        'joinCommunity': 'OUTGOING',
        'distribute': 'OUTGOING'
    }
}