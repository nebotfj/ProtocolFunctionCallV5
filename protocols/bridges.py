"""Cross-chain Bridge Functions"""

BRIDGE_FUNCTIONS = {
    'ARBITRUM': {
        'sendMessage': 'OUTGOING',
        'requestL2Transaction': 'OUTGOING',
        'finalizeWithdrawal': 'INCOMING',
        'depositETH': 'OUTGOING',
        'withdrawETH': 'INCOMING'
    },
    'OPTIMISM': {
        'depositTransaction': 'OUTGOING',
        'withdraw': 'INCOMING',
        'proveWithdrawal': 'BOTH',
        'finalizeWithdrawal': 'INCOMING'
    },
    'POLYGON': {
        'depositFor': 'OUTGOING',
        'exit': 'INCOMING',
        'withdraw': 'INCOMING',
        'depositEtherFor': 'OUTGOING'
    }
}