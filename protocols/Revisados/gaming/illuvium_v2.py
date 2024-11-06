"""Illuvium V2 Protocol Functions"""

ILLUVIUM_V2_FUNCTIONS = {
    'GAMEPLAY': {
        'startQuest': 'OUTGOING',
        'completeQuest': 'INCOMING',
        'craftItem': 'OUTGOING',
        'fightBattle': 'BOTH',
        'claimRewards': 'INCOMING'
    },
    'LAND': {
        'buildOnLand': 'OUTGOING',
        'harvestResources': 'INCOMING',
        'upgradeLand': 'OUTGOING',
        'tradeLand': 'BOTH'
    },
    'STAKING': {
        'stakeILV': 'OUTGOING',
        'unstakeILV': 'INCOMING',
        'claimYield': 'INCOMING',
        'lockStake': 'OUTGOING'
    }
}