"""Hop V2 Protocol Functions"""

HOP_V2_FUNCTIONS = {
    'BRIDGE': {
        'send': 'OUTGOING',
        'sendToL2': 'OUTGOING',
        'withdraw': 'INCOMING',
        'swapAndSend': 'BOTH'
    },
    'AMM': {
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING',
        'swap': 'BOTH',
        'flashLoan': 'BOTH'
    },
    'STAKING': {
        'stakeHOP': 'OUTGOING',
        'unstakeHOP': 'INCOMING',
        'claimRewards': 'INCOMING',
        'compoundRewards': 'OUTGOING'
    }
}