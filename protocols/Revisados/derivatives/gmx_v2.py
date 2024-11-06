"""GMX V2 Protocol Functions"""

GMX_V2_FUNCTIONS = {
    'TRADING': {
        'createOrder': 'OUTGOING',
        'updateOrder': 'OUTGOING',
        'cancelOrder': 'OUTGOING',
        'executeOrder': 'BOTH',
        'claimFunding': 'INCOMING'
    },
    'LIQUIDITY': {
        'createDeposit': 'OUTGOING',
        'cancelDeposit': 'OUTGOING',
        'executeDeposit': 'OUTGOING',
        'createWithdrawal': 'OUTGOING',
        'executeWithdrawal': 'INCOMING'
    },
    'REWARDS': {
        'claimableReward': 'NEUTRAL',
        'claimReward': 'INCOMING',
        'compound': 'OUTGOING',
        'handleRewards': 'BOTH'
    }
}