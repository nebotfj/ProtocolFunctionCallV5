"""Nexus Mutual Protocol Functions"""

NEXUS_MUTUAL_FUNCTIONS = {
    'COVERAGE': {
        'buyCover': 'OUTGOING',
        'submitClaim': 'OUTGOING',
        'redeemClaim': 'INCOMING',
        'withdrawExpiredCover': 'INCOMING'
    },
    'STAKING': {
        'stakeNXM': 'OUTGOING',
        'unstakeNXM': 'INCOMING',
        'claimRewards': 'INCOMING'
    },
    'GOVERNANCE': {
        'submitProposal': 'OUTGOING',
        'vote': 'OUTGOING',
        'claimRewards': 'INCOMING'
    }
}