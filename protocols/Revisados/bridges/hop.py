"""Hop Protocol Bridge Functions"""

HOP_FUNCTIONS = {
    'BRIDGE': {
        'send': 'OUTGOING',
        'sendToL2': 'OUTGOING',
        'withdraw': 'INCOMING',
        'swapAndSend': 'BOTH',
        'bonderFee': 'OUTGOING'
    },
    'AMM': {
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING',
        'swap': 'BOTH'
    },
    'REWARDS': {
        'stake': 'OUTGOING',
        'unstake': 'INCOMING',
        'claimRewards': 'INCOMING'
    }
}