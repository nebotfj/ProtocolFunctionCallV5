"""Aave Protocol Functions"""

AAVE_FUNCTIONS = {
    'LENDING': {
        'supply': 'OUTGOING',
        'borrow': 'INCOMING',
        'repay': 'OUTGOING',
        'withdraw': 'INCOMING',
        'depositAave': 'OUTGOING',
        'withdrawAave': 'INCOMING',
        'setUserUseReserveAsCollateral': 'OUTGOING',
        'swapBorrowRateMode': 'BOTH',
        'rebalanceStableBorrowRate': 'BOTH',
        'liquidationCall': 'BOTH'
    },
    'STAKING': {
        'stake': 'OUTGOING',
        'unstake': 'INCOMING',
        'cooldown': 'OUTGOING',
        'claimRewards': 'INCOMING',
        'redeem': 'INCOMING',
        'delegate': 'OUTGOING'
    },
    'FLASH_LOAN': {
        'flashLoan': 'BOTH',
        'flashLoanSimple': 'BOTH'
    },
    'GOVERNANCE': {
        'submitVote': 'OUTGOING',
        'delegate': 'OUTGOING',
        'proposalCreate': 'OUTGOING',
        'queueTransaction': 'OUTGOING',
        'executeTransaction': 'OUTGOING'
    }
}