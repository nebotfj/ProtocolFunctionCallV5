"""Token Creation Functions"""

TOKEN_CREATION_FUNCTIONS = {
    'ERC20': {
        'deployToken': 'OUTGOING',
        'setTokenomics': 'OUTGOING',
        'configureMinting': 'OUTGOING',
        'setupVesting': 'OUTGOING'
    },
    'GOVERNANCE': {
        'createDAO': 'OUTGOING',
        'setupTimelock': 'OUTGOING',
        'configureVoting': 'OUTGOING'
    },
    'DISTRIBUTION': {
        'airdrop': 'OUTGOING',
        'setupFarming': 'OUTGOING',
        'configureLiquidity': 'OUTGOING',
        'lockLiquidity': 'OUTGOING'
    }
}