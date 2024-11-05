"""Blur NFT Marketplace Functions"""

BLUR_FUNCTIONS = {
    'TRADING': {
        'executeBid': 'BOTH',
        'executeAsk': 'BOTH',
        'cancelOrder': 'OUTGOING',
        'bulkExecute': 'BOTH'
    },
    'LENDING': {
        'lendNFT': 'OUTGOING',
        'borrowNFT': 'INCOMING',
        'repayLoan': 'OUTGOING',
        'claimDefaultedNFT': 'INCOMING'
    },
    'STAKING': {
        'stakeBlur': 'OUTGOING',
        'unstakeBlur': 'INCOMING',
        'claimRewards': 'INCOMING'
    }
}