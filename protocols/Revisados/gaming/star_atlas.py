"""Star Atlas Protocol Functions"""

STAR_ATLAS_FUNCTIONS = {
    'GAMEPLAY': {
        'startMission': 'OUTGOING',
        'completeMission': 'INCOMING',
        'repairShip': 'OUTGOING',
        'upgradeShip': 'OUTGOING',
        'minePlanets': 'BOTH'
    },
    'MARKETPLACE': {
        'listAsset': 'OUTGOING',
        'buyAsset': 'OUTGOING',
        'createAuction': 'OUTGOING',
        'placeBid': 'OUTGOING',
        'claimAuction': 'INCOMING'
    },
    'STAKING': {
        'stakeATLAS': 'OUTGOING',
        'unstakeATLAS': 'INCOMING',
        'stakePOLIS': 'OUTGOING',
        'unstakePOLIS': 'INCOMING',
        'stakeLPTokens': 'OUTGOING',
        'unstakeLPTokens': 'INCOMING'
    }
}