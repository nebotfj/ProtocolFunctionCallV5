"""NFTX NFT Marketplace Functions"""

NFTX_FUNCTIONS = {
    'VAULT': {
        'createVault': 'OUTGOING',
        'mint': 'OUTGOING',
        'mintAndStake': 'OUTGOING',
        'redeem': 'BOTH',
        'redeemAndRemove': 'BOTH'
    },
    'STAKING': {
        'stake': 'OUTGOING',
        'unstake': 'INCOMING',
        'claimRewards': 'INCOMING',
        'stakeLiquidity': 'OUTGOING'
    },
    'TRADING': {
        'swap': 'BOTH',
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING',
        'flashLoan': 'BOTH'
    }
}