"""Ankr Liquid Staking Protocol Functions"""

ANKR_FUNCTIONS = {
    'STAKING': {
        'stake': 'OUTGOING',
        'unstake': 'INCOMING',
        'claimRewards': 'INCOMING',
        'compound': 'OUTGOING'
    },
    'LIQUID_STAKING': {
        'mintaETH': 'OUTGOING',
        'burnaETH': 'INCOMING',
        'convertToShares': 'BOTH',
        'convertToAssets': 'BOTH'
    },
    'GOVERNANCE': {
        'propose': 'OUTGOING',
        'vote': 'OUTGOING',
        'execute': 'OUTGOING'
    }
}