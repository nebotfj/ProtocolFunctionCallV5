"""GMX Protocol Functions"""

GMX_FUNCTIONS = {
    'TRADING': {
        'increasePosition': 'OUTGOING',
        'decreasePosition': 'INCOMING',
        'liquidatePosition': 'BOTH',
        'swap': 'BOTH'
    },
    'LIQUIDITY': {
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING',
        'stake': 'OUTGOING',
        'unstake': 'INCOMING'
    },
    'REWARDS': {
        'claimFees': 'INCOMING',
        'claimEsGmx': 'INCOMING',
        'stakeEsGmx': 'OUTGOING',
        'vestEsGmx': 'OUTGOING'
    },
    'REFERRALS': {
        'setReferralCode': 'OUTGOING',
        'claimReferralRewards': 'INCOMING',
        'compound': 'OUTGOING'
    }
}