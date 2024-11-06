"""API3 Protocol Functions"""

API3_FUNCTIONS = {
    'ORACLE': {
        'updateBeacon': 'OUTGOING',
        'readDataFeed': 'NEUTRAL',
        'requestData': 'OUTGOING',
        'fulfillRequest': 'INCOMING'
    },
    'STAKING': {
        'stakeAPI3': 'OUTGOING',
        'unstakeAPI3': 'INCOMING',
        'claimRewards': 'INCOMING'
    },
    'DAO': {
        'propose': 'OUTGOING',
        'vote': 'OUTGOING',
        'execute': 'OUTGOING'
    }
}