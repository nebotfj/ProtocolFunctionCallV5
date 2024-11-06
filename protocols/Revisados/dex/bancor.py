"""Bancor Protocol Functions"""

BANCOR_FUNCTIONS = {
    'TRADING': {
        'convertByPath': 'BOTH',
        'convert': 'BOTH',
        'rateByPath': 'NEUTRAL',
        'completeXConversion': 'BOTH'
    },
    'LIQUIDITY': {
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING',
        'addLiquidityFor': 'OUTGOING',
        'fundPool': 'OUTGOING'
    },
    'STAKING': {
        'stake': 'OUTGOING',
        'unstake': 'INCOMING',
        'claimRewards': 'INCOMING',
        'restake': 'OUTGOING'
    },
    'GOVERNANCE': {
        'propose': 'OUTGOING',
        'vote': 'OUTGOING',
        'execute': 'OUTGOING'
    }
}