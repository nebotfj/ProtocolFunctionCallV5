"""Rook Protocol Functions"""

ROOK_FUNCTIONS = {
    'TRADING': {
        'submitOrder': 'OUTGOING',
        'cancelOrder': 'OUTGOING',
        'settleOrder': 'BOTH',
        'batchSettlement': 'BOTH'
    },
    'STAKING': {
        'stakeROOK': 'OUTGOING',
        'unstakeROOK': 'INCOMING',
        'claimRewards': 'INCOMING'
    },
    'KEEPER': {
        'submitSolution': 'OUTGOING',
        'claimBounty': 'INCOMING'
    }
}