"""Splinterlands Protocol Functions"""

SPLINTERLANDS_FUNCTIONS = {
    'GAMEPLAY': {
        'startBattle': 'OUTGOING',
        'claimRewards': 'INCOMING',
        'purchaseCards': 'OUTGOING',
        'combineCards': 'OUTGOING'
    },
    'MARKETPLACE': {
        'listCard': 'OUTGOING',
        'buyCard': 'OUTGOING',
        'cancelListing': 'OUTGOING',
        'rentCard': 'BOTH'
    },
    'STAKING': {
        'stakeSPS': 'OUTGOING',
        'unstakeSPS': 'INCOMING',
        'claimStakingRewards': 'INCOMING'
    }
}