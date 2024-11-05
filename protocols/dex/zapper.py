"""Zapper.fi Protocol Functions"""

ZAPPER_FUNCTIONS = {
    'ZAPS': {
        'zapIn': 'OUTGOING',
        'zapOut': 'INCOMING',
        'multiZapIn': 'OUTGOING',
        'multiZapOut': 'INCOMING',
        'zapAcross': 'BOTH'
    },
    'FARMING': {
        'farmDeposit': 'OUTGOING',
        'farmWithdraw': 'INCOMING',
        'harvestRewards': 'INCOMING',
        'compoundFarm': 'OUTGOING'
    },
    'STAKING': {
        'stakeTokens': 'OUTGOING',
        'unstakeTokens': 'INCOMING',
        'claimRewards': 'INCOMING'
    }
}