"""The Graph Protocol Functions"""

THE_GRAPH_FUNCTIONS = {
    'INDEXING': {
        'stake': 'OUTGOING',
        'unstake': 'INCOMING',
        'delegate': 'OUTGOING',
        'undelegate': 'INCOMING'
    },
    'CURATION': {
        'signal': 'OUTGOING',
        'unsignal': 'INCOMING',
        'withdraw': 'INCOMING'
    },
    'REWARDS': {
        'claimIndexingRewards': 'INCOMING',
        'claimDelegationRewards': 'INCOMING'
    }
}