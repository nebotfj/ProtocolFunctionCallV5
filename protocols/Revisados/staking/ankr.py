"""Ankr Extended Protocol Functions"""

ANKR_EXTENDED_FUNCTIONS = {
    'STAKING': {
        'stake': 'OUTGOING',
        'unstake': 'INCOMING',
        'claimRewards': 'INCOMING',
        'restake': 'OUTGOING',
        'flashUnstake': 'BOTH'
    },
    'LIQUID_STAKING': {
        'mintAETH': 'OUTGOING',
        'burnAETH': 'INCOMING',
        'convertToShares': 'BOTH',
        'convertToAssets': 'BOTH'
    },
    'BRIDGE': {
        'bridgeAssets': 'OUTGOING',
        'claimBridged': 'INCOMING',
        'emergencyWithdraw': 'INCOMING'
    },
    'GOVERNANCE': {
        'propose': 'OUTGOING',
        'vote': 'OUTGOING',
        'execute': 'OUTGOING'
    }
}