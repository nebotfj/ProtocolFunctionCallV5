"""Drift Protocol Functions"""

DRIFT_FUNCTIONS = {
    'TRADING': {
        'openPosition': 'OUTGOING',
        'closePosition': 'INCOMING',
        'modifyPosition': 'BOTH',
        'placeTriggerOrder': 'OUTGOING',
        'cancelOrder': 'OUTGOING'
    },
    'LIQUIDITY': {
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING',
        'claimFees': 'INCOMING'
    },
    'STAKING': {
        'stakeDRIFT': 'OUTGOING',
        'unstakeDRIFT': 'INCOMING',
        'claimRewards': 'INCOMING'
    }
}