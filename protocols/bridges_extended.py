"""Extended Bridge Protocol Functions"""

BRIDGE_EXTENDED_FUNCTIONS = {
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
    },
    'WORMHOLE': {
        'transferTokens': 'OUTGOING',
        'completeTransfer': 'INCOMING',
        'attestToken': 'OUTGOING',
        'createWrapped': 'OUTGOING'
    },
    'STARGATE': {
        'swap': 'BOTH',
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING',
        'instantRedeemLocal': 'INCOMING'
    },
    'LAYERZERO': {
        'send': 'OUTGOING',
        'receive': 'INCOMING',
        'estimateFees': 'NEUTRAL',
        'validateTransactionProof': 'NEUTRAL'
    }
}