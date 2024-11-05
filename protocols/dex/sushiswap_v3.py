"""SushiSwap V3 Protocol Functions"""

SUSHISWAP_V3_FUNCTIONS = {
    'TRADING': {
        'exactInput': 'BOTH',
        'exactOutput': 'BOTH',
        'exactInputSingle': 'BOTH',
        'exactOutputSingle': 'BOTH'
    },
    'LIQUIDITY': {
        'mint': 'OUTGOING',
        'burn': 'INCOMING',
        'collect': 'INCOMING',
        'increaseLiquidity': 'OUTGOING',
        'decreaseLiquidity': 'INCOMING'
    },
    'CONCENTRATED': {
        'createPool': 'OUTGOING',
        'setFeeProtocol': 'OUTGOING',
        'collectProtocol': 'INCOMING'
    }
}