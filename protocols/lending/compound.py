"""Compound Protocol Functions"""

COMPOUND_FUNCTIONS = {
    'V2': {
        'LENDING': {
            'mint': {
                'direction': 'OUTGOING',
                'description': 'Mints cTokens by supplying the underlying asset',
                'method': '0xa0712d68'
            },
            'redeem': {
                'direction': 'INCOMING',
                'description': 'Redeems cTokens for the underlying asset',
                'method': '0xdb006a75'
            },
            'redeemUnderlying': {
                'direction': 'INCOMING',
                'description': 'Redeems a specific amount of underlying asset',
                'method': '0x852a12e3'
            },
            'borrow': {
                'direction': 'INCOMING',
                'description': 'Borrows the underlying asset against collateral',
                'method': '0xc5ebeaec'
            },
            'repayBorrow': {
                'direction': 'OUTGOING',
                'description': 'Repays borrowed assets',
                'method': '0x0e752702'
            },
            'repayBorrowBehalf': {
                'direction': 'OUTGOING',
                'description': 'Repays borrow on behalf of another address',
                'method': '0x2608f818'
            },
            'liquidateBorrow': {
                'direction': 'BOTH',
                'description': 'Liquidates an underwater position',
                'method': '0xf5e3c462'
            }
        },
        'MARKETS': {
            'enterMarkets': {
                'direction': 'OUTGOING',
                'description': 'Enters multiple markets for collateral usage',
                'method': '0xc2998238'
            },
            'exitMarket': {
                'direction': 'INCOMING',
                'description': 'Exits a market to stop using as collateral',
                'method': '0xede4edd0'
            },
            'supply': {
                'direction': 'OUTGOING',
                'description': 'Supplies assets to the protocol',
                'method': '0x1249c58b'
            },
            'withdraw': {
                'direction': 'INCOMING',
                'description': 'Withdraws supplied assets',
                'method': '0x2e1a7d4d'
            },
            'accrueInterest': {
                'direction': 'OUTGOING',
                'description': 'Updates interest accumulation for a market',
                'method': '0xa6afed95'
            }
        },
        'GOVERNANCE': {
            'delegate': {
                'direction': 'OUTGOING',
                'description': 'Delegates voting power to an address',
                'method': '0x5c19a95c'
            },
            'delegateBySig': {
                'direction': 'OUTGOING',
                'description': 'Delegates voting power with signature',
                'method': '0xc3cda520'
            },
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
            'castVoteBySig': {
                'direction': 'OUTGOING',
                'description': 'Casts vote using signature',
                'method': '0x3bccf4fd'
            },
            'queue': {
                'direction': 'OUTGOING',
                'description': 'Queues a successful proposal',
                'method': '0xddf0b009'
            },
            'execute': {
                'direction': 'OUTGOING',
                'description': 'Executes a queued proposal',
                'method': '0xfe0d94c1'
            },
            'cancel': {
                'direction': 'OUTGOING',
                'description': 'Cancels a proposal',
                'method': '0x40e58ee5'
            }
        }
    },
    'V3': {
        'LENDING': {
            'supply': {
                'direction': 'OUTGOING',
                'description': 'Supplies assets to the protocol with updated v3 mechanism',
                'method': '0x4b8a3529'
            },
            'withdraw': {
                'direction': 'INCOMING',
                'description': 'Withdraws supplied assets with updated v3 mechanism',
                'method': '0x0babd745'
            },
            'borrow': {
                'direction': 'INCOMING',
                'description': 'Borrows assets using new v3 risk model',
                'method': '0xc5ebeaec'
            },
            'repay': {
                'direction': 'OUTGOING',
                'description': 'Repays borrowed assets in v3',
                'method': '0x0e752702'
            },
            'liquidate': {
                'direction': 'BOTH',
                'description': 'Liquidates positions using v3 liquidation model',
                'method': '0xf5e3c462'
            }
        },
        'COMET': {
            'allow': {
                'direction': 'OUTGOING',
                'description': 'Permits an address to manage positions',
                'method': '0x7b510fe8'
            },
            'buyCollateral': {
                'direction': 'OUTGOING',
                'description': 'Purchases collateral from liquidation',
                'method': '0x0afb4c85'
            },
            'supplyTo': {
                'direction': 'OUTGOING',
                'description': 'Supplies assets to a specific account',
                'method': '0x474cf53d'
            },
            'withdrawTo': {
                'direction': 'INCOMING',
                'description': 'Withdraws assets to a specific account',
                'method': '0x9d3b9f2a'
            }
        }
    }
}
