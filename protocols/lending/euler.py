"""Euler Finance Protocol Functions"""

EULER_FUNCTIONS = {
    'V1': {
        'LENDING': {
            'deposit': {
                'direction': 'OUTGOING',
                'description': 'Deposits underlying tokens into Euler protocol',
                'method': '0x6e553f65'
            },
            'withdraw': {
                'direction': 'INCOMING',
                'description': 'Withdraws underlying tokens from Euler protocol',
                'method': '0x69328dec'
            },
            'borrow': {
                'direction': 'INCOMING',
                'description': 'Borrows tokens using collateral',
                'method': '0xc5ebeaec'
            },
            'repay': {
                'direction': 'OUTGOING',
                'description': 'Repays borrowed tokens',
                'method': '0x0e752702'
            },
            'mint': {
                'direction': 'OUTGOING',
                'description': 'Mints eTokens by supplying underlying asset',
                'method': '0x40c10f19'
            },
            'burn': {
                'direction': 'INCOMING',
                'description': 'Burns eTokens to receive underlying asset',
                'method': '0x9dc29fac'
            },
            'donateToReserves': {
                'direction': 'OUTGOING',
                'description': 'Donates assets to protocol reserves',
                'method': '0x8340f549'
            }
        },
        'COLLATERAL': {
            'enterMarket': {
                'direction': 'OUTGOING',
                'description': 'Enables an asset as collateral',
                'method': '0xc2998238'
            },
            'exitMarket': {
                'direction': 'INCOMING',
                'description': 'Disables an asset as collateral',
                'method': '0xede4edd0'
            },
            'transferCollateral': {
                'direction': 'BOTH',
                'description': 'Transfers collateral between accounts',
                'method': '0x0f2f630d'
            },
            'liquidate': {
                'direction': 'BOTH',
                'description': 'Liquidates unhealthy positions',
                'method': '0xf5e3c462'
            },
            'checkLiquidation': {
                'direction': 'NEUTRAL',
                'description': 'Checks if account can be liquidated',
                'method': '0x47ef3b3b'
            }
        },
        'RISK': {
            'updateRiskParameters': {
                'direction': 'OUTGOING',
                'description': 'Updates risk parameters for markets',
                'method': '0x43c4150d'
            },
            'setAssetConfig': {
                'direction': 'OUTGOING',
                'description': 'Configures asset parameters',
                'method': '0xd304f5ad'
            },
            'setPricingConfig': {
                'direction': 'OUTGOING',
                'description': 'Sets pricing configuration for assets',
                'method': '0x4437152a'
            },
            'setRiskTiers': {
                'direction': 'OUTGOING',
                'description': 'Sets risk tier for assets',
                'method': '0x1a7cd02c'
            }
        },
        'MARKETS': {
            'activateMarket': {
                'direction': 'OUTGOING',
                'description': 'Activates a new market',
                'method': '0x1c5aca87'
            },
            'deactivateMarket': {
                'direction': 'OUTGOING',
                'description': 'Deactivates an existing market',
                'method': '0x7d55c91e'
            }
        },
        'INTEREST_RATES': {
            'updateInterestRates': {
                'direction': 'OUTGOING',
                'description': 'Updates interest rate model parameters',
                'method': '0x6aa6ca96'
            },
            'setInterestRateModel': {
                'direction': 'OUTGOING',
                'description': 'Sets new interest rate model',
                'method': '0xf2b773f6'
            }
        }
    },
    'V2': {
        'LENDING': {
            'flashLoan': {
                'direction': 'BOTH',
                'description': 'Executes a flash loan',
                'method': '0x5cffe9de'
            },
            'deferLiquidityCheck': {
                'direction': 'BOTH',
                'description': 'Defers liquidity check for batch operations',
                'method': '0x7a5c8c3d'
            }
        },
        'RISK': {
            'setReferenceAsset': {
                'direction': 'OUTGOING',
                'description': 'Sets reference asset for market',
                'method': '0x9f510a9e'
            },
            'setRiskAdmin': {
                'direction': 'OUTGOING',
                'description': 'Sets risk administrator address',
                'method': '0x4f0d2d84'
            }
        },
        'GOVERNANCE': {
            'propose': {
                'direction': 'OUTGOING',
                'description': 'Creates governance proposal',
                'method': '0xda95691a'
            },
            'castVote': {
                'direction': 'OUTGOING',
                'description': 'Votes on proposal',
                'method': '0x56781388'
            }
        }
    }
}
