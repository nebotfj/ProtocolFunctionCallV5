"""Ember Sword Protocol Functions"""

EMBER_SWORD_FUNCTIONS = {
    'GAMEPLAY': {
        'startQuest': 'OUTGOING',
        'completeQuest': 'INCOMING',
        'craftItem': 'OUTGOING',
        'enhanceItem': 'OUTGOING',
        'claimRewards': 'INCOMING'
    },
    'LAND': {
        'purchaseLand': 'OUTGOING',
        'developLand': 'OUTGOING',
        'collectResources': 'INCOMING',
        'tradeLand': 'BOTH'
    },
    'MARKETPLACE': {
        'listItem': 'OUTGOING',
        'buyItem': 'OUTGOING',
        'cancelListing': 'OUTGOING',
        'acceptOffer': 'BOTH'
    },
    'STAKING': {
        'stakeLPTokens': 'OUTGOING',
        'unstakeLPTokens': 'INCOMING',
        'claimStakingRewards': 'INCOMING'
    }
}