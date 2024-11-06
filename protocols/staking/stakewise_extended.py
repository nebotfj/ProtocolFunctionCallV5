"""StakeWise Extended Protocol Functions"""

STAKEWISE_EXTENDED_FUNCTIONS = {
    'STAKING': {
        'stake': 'OUTGOING',
        'unstake': 'INCOMING',
        'claimRewards': 'INCOMING',
        'compound': 'OUTGOING',
        'requestWithdrawal': 'OUTGOING'
    },
    'POOL': {
        'joinPool': 'OUTGOING',
        'exitPool': 'INCOMING',
        'swapExactTokensForTokens': 'BOTH',
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING'
    },
    'MERKLE': {
        'claimMerkleRewards': 'INCOMING',
        'verifyProof': 'NEUTRAL',
        'updateMerkleRoot': 'OUTGOING'
    },
    'GOVERNANCE': {
        'propose': 'OUTGOING',
        'vote': 'OUTGOING',
        'execute': 'OUTGOING',
        'delegate': 'OUTGOING'
    }
}