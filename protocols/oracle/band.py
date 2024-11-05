"""Band Protocol Functions"""

BAND_FUNCTIONS = {
    'ORACLE': {
        'relayBlock': 'OUTGOING',
        'getReferenceData': 'NEUTRAL',
        'getReferenceDataBulk': 'NEUTRAL',
        'requestData': 'OUTGOING'
    },
    'STAKING': {
        'delegate': 'OUTGOING',
        'undelegate': 'INCOMING',
        'redelegate': 'BOTH',
        'claimRewards': 'INCOMING'
    },
    'GOVERNANCE': {
        'propose': 'OUTGOING',
        'vote': 'OUTGOING',
        'execute': 'OUTGOING'
    }
}