"""Liquid Staking Protocol Functions"""

LIQUID_STAKING_FUNCTIONS = {
    'LIDO': {
        'submit': 'OUTGOING',
        'withdraw': 'INCOMING',
        'requestWithdrawals': 'OUTGOING',
        'claimWithdrawals': 'INCOMING'
    },
    'ROCKETPOOL': {
        'deposit': 'OUTGOING',
        'withdraw': 'INCOMING',
        'stake': 'OUTGOING',
        'claimRewards': 'INCOMING',
        'claimRPL': 'INCOMING'
    },
    'STAKEWISE': {
        'stake': 'OUTGOING',
        'unstake': 'INCOMING',
        'claimRewards': 'INCOMING',
        'compound': 'OUTGOING'
    },
    'FRAX': {
        'deposit': 'OUTGOING',
        'withdraw': 'INCOMING',
        'claimRewards': 'INCOMING',
        'lockStake': 'OUTGOING'
    },
    'ANKR': {
        'stake': 'OUTGOING',
        'unstake': 'INCOMING',
        'claimRewards': 'INCOMING',
        'flashUnstake': 'BOTH'
    },
    'SWELL': {
        'deposit': 'OUTGOING',
        'withdraw': 'INCOMING',
        'harvest': 'INCOMING'
    },
    'STADER': {
        'stake': 'OUTGOING',
        'unstake': 'INCOMING',
        'claimRewards': 'INCOMING',
        'convertToShares': 'BOTH'
    },
    'OETH': {
        'mint': 'OUTGOING',
        'redeem': 'INCOMING',
        'rebase': 'NEUTRAL',
        'claimYield': 'INCOMING'
    },
    'MANTLE': {
        'deposit': 'OUTGOING',
        'withdraw': 'INCOMING',
        'claimRewards': 'INCOMING'
    }
}