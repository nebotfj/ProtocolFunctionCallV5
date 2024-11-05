"""RocketPool Staking Functions"""

ROCKETPOOL_FUNCTIONS = {
    'NODE': {
        'registerNode': 'OUTGOING',
        'depositNode': 'OUTGOING',
        'stakeRPL': 'OUTGOING',
        'withdrawRPL': 'INCOMING'
    },
    'MINIPOOL': {
        'createMinipool': 'OUTGOING',
        'stakeMinipool': 'OUTGOING',
        'withdrawMinipool': 'INCOMING',
        'closeMinipool': 'BOTH'
    },
    'REWARDS': {
        'claimNodeRewards': 'INCOMING',
        'claimRPLRewards': 'INCOMING',
        'distributeRewards': 'OUTGOING'
    }
}