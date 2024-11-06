"""Additional DEX Protocol Functions"""

ADDITIONAL_DEX_FUNCTIONS = {
    'KYBER': {
        'swapExactTokensForTokens': 'BOTH',
        'swapTokensForExactTokens': 'BOTH',
        'swapExactETHForTokens': 'OUTGOING',
        'swapTokensForExactETH': 'BOTH',
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING'
    },
    'ZAPPER': {
        'zap': 'BOTH',
        'zapIn': 'OUTGOING',
        'zapOut': 'INCOMING',
        'zapAcross': 'BOTH',
        'zapInTokens': 'OUTGOING',
        'zapOutTokens': 'INCOMING'
    },
    'HARVEST': {
        'deposit': 'OUTGOING',
        'withdraw': 'INCOMING',
        'stake': 'OUTGOING',
        'unstake': 'INCOMING',
        'harvest': 'INCOMING',
        'claimRewards': 'INCOMING'
    }
}