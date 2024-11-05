"""Lyra Options Protocol Functions"""

LYRA_FUNCTIONS = {
    'OPTIONS': {
        'openPosition': 'OUTGOING',
        'closePosition': 'INCOMING',
        'exerciseOption': 'BOTH',
        'settleExpired': 'INCOMING'
    },
    'LIQUIDITY': {
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING',
        'claimRewards': 'INCOMING'
    },
    'STAKING': {
        'stakeLYRA': 'OUTGOING',
        'unstakeLYRA': 'INCOMING',
        'claimStakingRewards': 'INCOMING'
    }
}