"""Maverick DEX Functions"""

MAVERICK_FUNCTIONS = {
    'TRADING': {
        'swap': 'BOTH',
        'batchSwap': 'BOTH',
        'flashSwap': 'BOTH'
    },
    'LIQUIDITY': {
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING',
        'addLiquidityBinning': 'OUTGOING',
        'removeLiquidityBinning': 'INCOMING'
    },
    'STAKING': {
        'stake': 'OUTGOING',
        'unstake': 'INCOMING',
        'claimRewards': 'INCOMING'
    }
}