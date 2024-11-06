"""Frax Extended Protocol Functions"""

FRAX_EXTENDED_FUNCTIONS = {
    'AMO': {
        'mintFrax': 'OUTGOING',
        'burnFrax': 'INCOMING',
        'recollateralize': 'OUTGOING',
        'buybackFrax': 'OUTGOING'
    },
    'STAKING': {
        'stakeFxs': 'OUTGOING',
        'unstakeFxs': 'INCOMING',
        'claimRewards': 'INCOMING',
        'lockStake': 'OUTGOING',
        'withdrawLocked': 'INCOMING'
    },
    'LENDING': {
        'borrow': 'INCOMING',
        'repay': 'OUTGOING',
        'liquidate': 'BOTH',
        'addCollateral': 'OUTGOING',
        'removeCollateral': 'INCOMING'
    },
    'GOVERNANCE': {
        'propose': 'OUTGOING',
        'vote': 'OUTGOING',
        'execute': 'OUTGOING',
        'delegate': 'OUTGOING'
    }
}