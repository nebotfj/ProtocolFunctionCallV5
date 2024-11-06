"""Redacted Protocol Functions"""

REDACTED_FUNCTIONS = {
    'STAKING': {
        'stakeBTRFLY': 'OUTGOING',
        'unstakeBTRFLY': 'INCOMING',
        'claimRewards': 'INCOMING',
        'compoundRewards': 'OUTGOING'
    },
    'HIDDEN_HAND': {
        'claimBribes': 'INCOMING',
        'voteBribes': 'OUTGOING',
        'proposeBribe': 'OUTGOING'
    },
    'TREASURY': {
        'proposePurchase': 'OUTGOING',
        'executePurchase': 'OUTGOING',
        'harvestYield': 'INCOMING'
    }
}