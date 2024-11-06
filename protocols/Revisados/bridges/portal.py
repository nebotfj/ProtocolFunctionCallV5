"""Portal (Wormhole) Bridge Functions"""

PORTAL_FUNCTIONS = {
    'BRIDGE': {
        'transferTokens': 'OUTGOING',
        'completeTransfer': 'INCOMING',
        'transferNFT': 'OUTGOING',
        'redeemNFT': 'INCOMING'
    },
    'GOVERNANCE': {
        'registerChain': 'OUTGOING',
        'upgradeContract': 'OUTGOING',
        'setGuardian': 'OUTGOING'
    },
    'RELAYER': {
        'submitVAA': 'OUTGOING',
        'redeemOnEth': 'INCOMING',
        'createWrapped': 'OUTGOING'
    }
}