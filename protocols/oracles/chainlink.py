"""Chainlink Protocol Functions"""

CHAINLINK_FUNCTIONS = {
    'ORACLE': {
        'latestRoundData': 'NEUTRAL',
        'getRoundData': 'NEUTRAL',
        'getAnswer': 'NEUTRAL',
        'getTimestamp': 'NEUTRAL'
    },
    'KEEPER': {
        'checkUpkeep': 'NEUTRAL',
        'performUpkeep': 'OUTGOING',
        'registerUpkeep': 'OUTGOING',
        'cancelUpkeep': 'OUTGOING'
    },
    'VRF': {
        'requestRandomness': 'OUTGOING',
        'fulfillRandomness': 'INCOMING',
        'requestRandomWords': 'OUTGOING',
        'fulfillRandomWords': 'INCOMING'
    }
}