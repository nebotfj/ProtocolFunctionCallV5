"""0x Protocol Functions"""

ZEROEX_FUNCTIONS = {
    'TRADING': {
        'fillOrder': 'BOTH',
        'cancelOrder': 'OUTGOING',
        'batchFillOrders': 'BOTH',
        'matchOrders': 'BOTH'
    },
    'RFQ': {
        'requestQuote': 'NEUTRAL',
        'fillRfqOrder': 'BOTH',
        'cancelRfqOrder': 'OUTGOING'
    },
    'STAKING': {
        'stake': 'OUTGOING',
        'unstake': 'INCOMING',
        'withdrawDelegatorRewards': 'INCOMING'
    },
    'BRIDGE': {
        'bridgeTransfer': 'OUTGOING',
        'transformERC20': 'BOTH'
    }
}