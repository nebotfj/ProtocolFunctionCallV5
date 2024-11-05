PROTOCOL_FUNCTIONS = {
    # ... (previous protocols remain the same) ...

    'ORIGIN': {
        'FUNCTIONS': [
            # OUSD Functions
            'mint',
            'redeem',
            'redeemAll',
            'depositYield',
            'claimYield',
            'rebase',
            'transferFrom',
            
            # Origin Dollar Governance
            'propose',
            'queue',
            'execute',
            'cancel',
            'castVote',
            'delegate',
            
            # Vault Functions
            'depositAndStake',
            'withdrawAndUnstake',
            'harvest',
            'rebalance',
            'reallocate',
            
            # Staking
            'stake',
            'unstake',
            'getReward',
            'exit',
            'claimRewards',
            
            # NFT Marketplace
            'createListing',
            'createOffer',
            'acceptOffer',
            'cancelListing',
            'cancelOffer',
            'finalize',
            'buyNFT',
            'settlePayment',
            
            # Launchpad
            'participate',
            'claim',
            'refund',
            'finalizePool',
            
            # Story Protocol
            'registerIP',
            'licenseTo',
            'createDerivative',
            'verifyRights',
            'collectRoyalties'
        ]
    }
}