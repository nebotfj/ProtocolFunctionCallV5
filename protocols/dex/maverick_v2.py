"""Maverick V2 Protocol Functions"""

MAVERICK_V2_FUNCTIONS = {
    'TRADING': {
        'swap': 'BOTH',
        'batchSwap': 'BOTH',
        'flashSwap': 'BOTH',
        'dynamicSwap': 'BOTH'
    },
    'LIQUIDITY': {
        'addLiquidity': 'OUTGOING',
        'removeLiquidity': 'INCOMING',
        'addLiquidityBinning': 'OUTGOING',
        'removeLiquidityBinning': 'INCOMING',
        'migrateLiquidity': 'BOTH'
    },
    'STAKING': {
        'stake': 'OUTGOING',
        'unstake': 'INCOMING',
        'claimRewards': 'INCOMING',
        'compoundRewards': 'OUTGOING'
    }
}