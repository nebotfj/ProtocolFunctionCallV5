"""Synapse Protocol Bridge Functions"""

SYNAPSE_FUNCTIONS = {
    'BRIDGE': {
        'bridge': 'OUTGOING',
        'redeem': 'INCOMING',
        'swapAndBridge': 'BOTH',
        'bridgeAndSwap': 'BOTH'
    },
    'POOLS': {
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING',
        'swap': 'BOTH',
        'flashLoan': 'BOTH'
    },
    'STAKING': {
        'stake': 'OUTGOING',
        'unstake': 'INCOMING',
        'harvest': 'INCOMING'
    }
}