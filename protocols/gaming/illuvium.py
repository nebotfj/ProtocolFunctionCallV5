"""Illuvium Protocol Functions"""

ILLUVIUM_FUNCTIONS = {
    'GAMEPLAY': {
        'captureIlluvial': 'OUTGOING',
        'fightBattle': 'BOTH',
        'claimRewards': 'INCOMING',
        'upgradeIlluvial': 'OUTGOING'
    },
    'STAKING': {
        'stakeILV': 'OUTGOING',
        'unstakeILV': 'INCOMING',
        'claimYield': 'INCOMING',
        'lockStake': 'OUTGOING'
    },
    'LAND': {
        'purchaseLand': 'OUTGOING',
        'buildOnLand': 'OUTGOING',
        'harvestResources': 'INCOMING',
        'tradeLand': 'BOTH'
    },
    'GOVERNANCE': {
        'propose': 'OUTGOING',
        'vote': 'OUTGOING',
        'execute': 'OUTGOING'
    }
}