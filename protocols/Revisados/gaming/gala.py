"""Gala Games Protocol Functions"""

GALA_FUNCTIONS = {
    'NODES': {
        'operateNode': 'OUTGOING',
        'claimNodeRewards': 'INCOMING',
        'upgradeNode': 'OUTGOING',
        'migrateNode': 'BOTH'
    },
    'GAMING': {
        'purchaseItem': 'OUTGOING',
        'sellItem': 'INCOMING',
        'useItem': 'OUTGOING',
        'claimRewards': 'INCOMING'
    },
    'STAKING': {
        'stakeGALA': 'OUTGOING',
        'unstakeGALA': 'INCOMING',
        'claimStakingRewards': 'INCOMING'
    }
}