CATEGORIES = {
    'LIQUIDITY': ['add_liquidity', 'remove_liquidity', 'addLiquidity', 'removeLiquidity'],
    'SWAP': ['swap', 'unoswap', 'swapExact', 'swapBorrow', 'tokenToToken', 'ethToToken'],
    'STAKING': ['stake', 'unstake', 'cooldown', 'claim', 'vote', 'delegate'],
    'LENDING': ['borrow', 'repay', 'supply', 'withdraw', 'depositAave', 'withdrawAave'],
    'POOL': ['joinPool', 'exitPool', 'depositPool'],
    'GOVERNANCE': ['vote', 'delegate', 'propose', 'execute'],
    'BRIDGE': ['sendMessage', 'requestL2Transaction'],
    'TOKEN': ['mint', 'burn', 'approve', 'transfer', 'safeTransferFrom'],
    'FLASH_LOAN': ['flashLoan'],
    'MIGRATION': ['migrate', 'migrateAll', 'migrateFrom'],
    'UTILITY': ['multicall', 'batch', 'build', 'create', 'register'],
    'DEPOSIT': ['deposit', 'depositAll', 'depositETH', 'depositBase', 'depositQuote', 'depositSavings'],
    'WITHDRAWAL': ['withdraw', 'withdrawAll', 'withdrawETH', 'withdrawBase', 'withdrawQuote', 'withdrawFunds']
}

def get_direction(operation: str) -> str:
    if operation.endswith('_in'):
        return 'INCOMING (funds entering wallet)'
    if operation.endswith('_out'):
        return 'OUTGOING (funds leaving wallet)'
    return 'DIRECTION UNKNOWN'

def classify_operation(operation: str) -> str:
    base_name = operation.lower().replace('_out', '').replace('_in', '')
    
    for category, patterns in CATEGORIES.items():
        if any(pattern.lower() in base_name for pattern in patterns):
            return category
    
    return 'UNKNOWN'

def analyze_operation(function_call: str) -> None:
    category = classify_operation(function_call)
    direction = get_direction(function_call)
    print(f"Operation: {function_call}")
    print(f"Category: {category}")
    print(f"Direction: {direction}")
    print("---")

def main():
    # Test examples
    test_operations = [
        'add_liquidity_out',
        'swapExactETHForTokens_out',
        'ETH transfer_in',
        'borrow_out',
        'claim_in',
        'flashLoan_out',
        'depositETH_out',
        'withdrawAll_out'
    ]

    print("Operation Type Classifier\n")
    for op in test_operations:
        analyze_operation(op)

    # Interactive mode
    print("\nInteractive Mode - Enter function calls to classify")
    print("Type 'exit' to quit")
    
    while True:
        user_input = input("\nEnter a function call to classify: ").strip()
        if user_input.lower() == 'exit':
            break
        analyze_operation(user_input)

if __name__ == "__main__":
    main()