"""Wallfair Protocol Functions"""

WALLFAIR_FUNCTIONS = {
    'BETTING': {
        'createEvent': 'OUTGOING',
        'placeBet': 'OUTGOING',
        'claimReward': 'INCOMING',
        'cancelBet': 'INCOMING'
    },
    'STAKING': {
        'stakeWFAIR': 'OUTGOING',
        'unstakeWFAIR': 'INCOMING',
        'harvestRewards': 'INCOMING'
    },
    'GOVERNANCE': {
        'createProposal': 'OUTGOING',
        'vote': 'OUTGOING',
        'executeProposal': 'OUTGOING'
    }
}