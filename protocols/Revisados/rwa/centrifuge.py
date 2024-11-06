"""Centrifuge Protocol Functions"""

CENTRIFUGE_FUNCTIONS = {
    'ASSETS': {
        'createAsset': 'OUTGOING',
        'updateAsset': 'OUTGOING',
        'mintNFT': 'OUTGOING',
        'transferAsset': 'BOTH'
    },
    'FINANCING': {
        'createPool': 'OUTGOING',
        'invest': 'OUTGOING',
        'redeem': 'INCOMING',
        'claimRewards': 'INCOMING'
    },
    'STAKING': {
        'stakeCFG': 'OUTGOING',
        'unstakeCFG': 'INCOMING',
        'claimStakingRewards': 'INCOMING'
    }
}