"""Basic Ethereum Transaction Functions"""

ETHEREUM_BASE_FUNCTIONS = {
    'TRANSACTIONS': {
        'transfer': 'OUTGOING',
        'transferFrom': 'OUTGOING',
        'approve': 'OUTGOING',
        'increaseAllowance': 'OUTGOING',
        'decreaseAllowance': 'OUTGOING',
        'permit': 'OUTGOING'
    },
    'ERC20': {
        'mint': 'OUTGOING',
        'burn': 'OUTGOING',
        'burnFrom': 'OUTGOING',
        'pause': 'OUTGOING',
        'unpause': 'OUTGOING'
    },
    'ERC721': {
        'safeMint': 'OUTGOING',
        'safeTransferFrom': 'OUTGOING',
        'setApprovalForAll': 'OUTGOING',
        'approve': 'OUTGOING',
        'burn': 'OUTGOING'
    },
    'ERC1155': {
        'safeTransferFrom': 'OUTGOING',
        'safeBatchTransferFrom': 'OUTGOING',
        'setApprovalForAll': 'OUTGOING',
        'mint': 'OUTGOING',
        'mintBatch': 'OUTGOING',
        'burn': 'OUTGOING',
        'burnBatch': 'OUTGOING'
    },
    'MULTICALL': {
        'aggregate': 'BOTH',
        'tryAggregate': 'BOTH',
        'blockAndAggregate': 'BOTH'
    },
    'PROXY': {
        'upgradeTo': 'OUTGOING',
        'upgradeToAndCall': 'OUTGOING',
        'changeAdmin': 'OUTGOING',
        'implementation': 'NEUTRAL'
    }
}