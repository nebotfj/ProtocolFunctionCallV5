"""Synthetix Protocol Functions"""

SYNTHETIX_FUNCTIONS = {
    'TRADING': {
        'exchange': 'BOTH',
        'exchangeWithTracking': 'BOTH',
        'exchangeWithVirtual': 'BOTH'
    },
    'STAKING': {
        'stake': 'OUTGOING',
        'unstake': 'INCOMING',
        'claimRewards': 'INCOMING',
        'mint': 'OUTGOING',
        'burn': 'INCOMING'
    },
    'COLLATERAL': {
        'addCollateral': 'OUTGOING',
        'removeCollateral': 'INCOMING',
        'liquidate': 'BOTH'
    }
}