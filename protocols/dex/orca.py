"""Orca Protocol Functions"""

ORCA_FUNCTIONS = {
    'SWAP': {
        'swap': 'BOTH',
        'swapBaseIn': 'BOTH',
        'swapBaseOut': 'BOTH'
    },
    'WHIRLPOOLS': {
        'openPosition': 'OUTGOING',
        'closePosition': 'INCOMING',
        'modifyPosition': 'BOTH',
        'collectFees': 'INCOMING'
    },
    'FARMING': {
        'deposit': 'OUTGOING',
        'withdraw': 'INCOMING',
        'harvest': 'INCOMING',
        'compound': 'OUTGOING'
    },
    'DOUBLE_DIP': {
        'depositDD': 'OUTGOING',
        'withdrawDD': 'INCOMING',
        'harvestDD': 'INCOMING'
    }
}