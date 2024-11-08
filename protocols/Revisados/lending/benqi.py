"""Benqi Protocol Functions"""

BENQI_FUNCTIONS = {
    'V1': {
        'LENDING': {
            'supply': {
                'direction': 'OUTGOING',
                'description': 'Supplies assets to the Benqi protocol as collateral',
                'method': '0x1249c58b'
            },
            'withdraw': {
                'direction': 'INCOMING',
                'description': 'Withdraws supplied assets from the protocol',
                'method': '0x2e1a7d4d'
            },
            'borrow': {
                'direction': 'INCOMING',
                'description': 'Borrows assets against supplied collateral',
                'method': '0xc5ebeaec'
            },
            'repay': {
                'direction': 'OUTGOING',
                'description': 'Repays borrowed assets to the protocol',
                'method': '0x0e752702'
            },
            'liquidate': {
                'direction': 'BOTH',
                'description': 'Liquidates undercollateralized positions',
                'method': '0xf0988da6'
            },
            'enterMarkets': {
                'direction': 'OUTGOING',
                'description': 'Enables supplied assets to be used as collateral',
                'method': '0xc2998238'
            },
            'exitMarket': {
                'direction': 'OUTGOING',
                'description': 'Disables an asset from being used as collateral',
                'method': '0xede4edd0'
            }
        },
        'STAKING': {
            'stake': {
                'direction': 'OUTGOING',
                'description': 'Stakes QI tokens in the protocol',
                'method': '0xa694fc3a'
            },
            'unstake': {
                'direction': 'INCOMING',
                'description': 'Withdraws staked QI tokens',
                'method': '0x2e17de78'
            },
            'claimRewards': {
                'direction': 'INCOMING',
                'description': 'Claims accumulated staking rewards',
                'method': '0xe09c3b93'
            },
            'delegate': {
                'direction': 'OUTGOING',
                'description': 'Delegates voting power to an address',
                'method': '0x5c19a95c'
            },
            'getRewardsByMarket': {
                'direction': 'INCOMING',
                'description': 'Claims rewards for specific markets',
                'method': '0x6e85f13e'
            }
        },
        'GOVERNANCE': {
            'propose': {
                'direction': 'OUTGOING',
                'description': 'Creates a new governance proposal',
                'method': '0xda95691a'
            },
            'vote': {
                'direction': 'OUTGOING',
                'description': 'Casts vote on active proposals',
                'method': '0x0121b93f'
            },
            'execute': {
                'direction': 'OUTGOING',
                'description': 'Executes a successful proposal',
                'method': '0xfe0d94c1'
            },
            'cancel': {
                'direction': 'OUTGOING',
                'description': 'Cancels a pending proposal',
                'method': '0x40e58ee5'
            },
            'queue': {
                'direction': 'OUTGOING',
                'description': 'Queues a successful proposal for execution',
                'method': '0xddf0b009'
            }
        },
        'SAFETY_MODULE': {
            'cooldown': {
                'direction': 'OUTGOING',
                'description': 'Initiates cooldown period for unstaking',
                'method': '0x7210e1ea'
            },
            'processRewards': {
                'direction': 'INCOMING',
                'description': 'Processes and distributes safety module rewards',
                'method': '0x2ce5c7a0'
            }
        }
    }
}
