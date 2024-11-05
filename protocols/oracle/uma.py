"""UMA Protocol Functions"""

UMA_FUNCTIONS = {
    'ORACLE': {
        'requestPrice': 'OUTGOING',
        'proposePrice': 'OUTGOING',
        'disputePrice': 'OUTGOING',
        'settleRequest': 'INCOMING'
    },
    'VOTING': {
        'commitVote': 'OUTGOING',
        'revealVote': 'OUTGOING',
        'claimRewards': 'INCOMING'
    },
    'KPI_OPTIONS': {
        'createOption': 'OUTGOING',
        'exercise': 'BOTH',
        'settle': 'INCOMING'
    }
}