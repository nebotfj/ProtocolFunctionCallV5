"""Beefy Finance Protocol Functions"""

BEEFY_FUNCTIONS = {
    'VAULT': {
        'deposit': 'OUTGOING',
        'withdraw': 'INCOMING',
        'depositAll': 'OUTGOING',
        'withdrawAll': 'INCOMING',
        'getPricePerFullShare': 'NEUTRAL'
    },
    'BOOST': {
        'stake': 'OUTGOING',
        'unstake': 'INCOMING',
        'stakeLPTokens': 'OUTGOING',
        'unstakeLPTokens': 'INCOMING',
        'claimRewards': 'INCOMING'
    },
    'ZAPS': {
        'beefIn': 'OUTGOING',
        'beefOut': 'INCOMING',
        'beefInETH': 'OUTGOING',
        'beefOutETH': 'INCOMING'
    }
}