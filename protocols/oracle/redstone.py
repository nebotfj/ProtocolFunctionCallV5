"""Redstone Protocol Functions"""

REDSTONE_FUNCTIONS = {
    'ORACLE': {
        'updatePrices': 'OUTGOING',
        'getPrices': 'NEUTRAL',
        'signData': 'OUTGOING',
        'verifySignatures': 'NEUTRAL'
    },
    'CACHE': {
        'cacheValues': 'OUTGOING',
        'getCachedValues': 'NEUTRAL',
        'updateCache': 'OUTGOING'
    },
    'AGGREGATION': {
        'aggregateValues': 'NEUTRAL',
        'calculateMedian': 'NEUTRAL',
        'validateDataFeed': 'NEUTRAL'
    }
}