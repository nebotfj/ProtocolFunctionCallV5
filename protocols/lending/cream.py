"""Cream Finance Protocol Functions"""

CREAM_FUNCTIONS = {
    'V1': {
        'LENDING': {
            'mint': {
                'direction': 'OUTGOING',
                'description': 'Mints crTokens by supplying the underlying asset',
                'method': '0xa0712d68'
            },
            'redeem': {
                'direction': 'INCOMING',
                'description': 'Redeems crTokens for the underlying asset',
                'method': '0xdb006a75'
            },
            'redeemUnderlying': {
                'direction': 'INCOMING',
                'description': 'Redeems a specific amount of underlying asset',
                'method': '0x852a12e3'
            },
            'borrow': {
                'direction': 'INCOMING',
                'description': 'Borrows the underlying asset using collateral',
                'method': '0xc5ebeaec'
            },
            'repay': {
                'direction': 'OUTGOING',
                'description': 'Repays borrowed assets',
                'method': '0x0e752702'
            },
            'repayBehalf': {
                'direction': 'OUTGOING',
                'description': 'Repays borrow on behalf of another address',
                'method': '0x2608f818'
            },
            'liquidate': {
                'direction': 'BOTH',
                'description': 'Liquidates an underwater position',
                'method': '0xf5e3c462'
            }
        },
        'MARKETS': {
            'enterMarkets': {
                'direction': 'OUTGOING',
                'description': 'Enters multiple markets for using as collateral',
                'method': '0xc2998238'
            },
            'exitMarket': {
                'direction': 'INCOMING',
                'description': 'Exits a market to stop using as collateral',
                'method': '0xede4edd0'
            },
            'getAccountLiquidity': {
                'direction': 'NEUTRAL',
                'description': 'Gets account liquidity information',
                'method': '0x5ec88c79'
            },
            'getAssetsIn': {
                'direction': 'NEUTRAL',
                'description': 'Gets all markets an account is in',
                'method': '0xabfceffc'
            },
            'checkMembership': {
                'direction': 'NEUTRAL',
                'description': 'Checks if an account is in a market',
                'method': '0x929fe9a1'
            }
        },
        'GOVERNANCE': {
            'propose': {
                'direction': 'OUTGOING',
                'description': 'Creates a new governance proposal',
                'method': '0xda95691a'
            },
            'castVote': {
                'direction': 'OUTGOING',
                'description': 'Casts vote on a proposal',
                'method': '0x56781388'
            },
            'castVoteWithReason': {
                'direction': 'OUTGOING',
                'description': 'Casts vote with explanation',
                'method': '0x7b3c71d3'
            },
            'execute': {
                'direction': 'OUTGOING',
                'description': 'Executes a queued proposal',
                'method': '0xfe0d94c1'
            },
            'queue': {
                'direction': 'OUTGOING',
                'description': 'Queues a successful proposal',
                'method': '0xddf0b009'
            },
            'cancel': {
                'direction': 'OUTGOING',
                'description': 'Cancels a proposal',
                'method': '0x40e58ee5'
            }
        }
    },
    'V2': {
        'LENDING': {
            'supply': {
                'direction': 'OUTGOING',
                'description': 'Supplies assets with updated v2 mechanism',
                'method': '0x4b8a3529'
            },
            'withdraw': {
                'direction': 'INCOMING',
                'description': 'Withdraws supplied assets with v2 mechanism',
                'method': '0x0babd745'
            },
            'borrow': {
                'direction': 'INCOMING',
                'description': 'Borrows assets using v2 risk model',
                'method': '0xc5ebeaec'
            },
            'repay': {
                'direction': 'OUTGOING',
                'description': 'Repays borrowed assets in v2',
                'method': '0x0e752702'
            }
        },
        'IRON_BANK': {
            'creditLimits': {
                'direction': 'NEUTRAL',
                'description': 'Checks credit limits for whitelisted accounts',
                'method': '0x4ce4c774'
            },
            'setCreditLimit': {
                'direction': 'OUTGOING',
                'description': 'Sets credit limit for whitelisted address',
                'method': '0xd91921ed'
            }
        },
        'FLASH_LOAN': {
            'flashLoan': {
                'direction': 'BOTH',
                'description': 'Executes a flash loan',
                'method': '0x5cffe9de'
            }
        }
    }
}
