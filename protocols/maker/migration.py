"""MakerDAO SCD to MCD Migration Functions"""

MAKER_MIGRATION_FUNCTIONS = {
    'SCD_SHUTDOWN': {
        'shutdownSCD': 'OUTGOING',
        'redeemSCD': 'INCOMING',
        'swapSaiToDai': 'BOTH'
    },
    'MCD_MIGRATION': {
        'migrateToMCD': 'BOTH',
        'migrateCDP': 'BOTH',
        'migrateProxy': 'BOTH'
    },
    'COLLATERAL': {
        'migrateCollateral': 'BOTH',
        'withdrawCollateral': 'INCOMING',
        'paybackDebt': 'OUTGOING'
    }
}