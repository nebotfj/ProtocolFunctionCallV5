from protocol_analyzer import ProtocolAnalyzer
from operation_classifier import analyze_operation

def main():
    print("DeFi Protocol Analysis Tools")
    print("=" * 50)
    print("\nAvailable Tools:")
    print("1. Protocol Analyzer")
    print("2. Operation Classifier")
    print("3. Exit")

    while True:
        choice = input("\nSelect a tool (1-3): ").strip()

        if choice == '1':
            analyzer = ProtocolAnalyzer()
            analyzer.main()
        
        elif choice == '2':
            print("\nOperation Classifier")
            print("Enter 'exit' to return to main menu")
            while True:
                operation = input("\nEnter operation to classify: ").strip()
                if operation.lower() == 'exit':
                    break
                analyze_operation(operation)
        
        elif choice == '3':
            print("\nThank you for using DeFi Protocol Analysis Tools!")
            break
        
        else:
            print("\nInvalid choice. Please select 1-3.")

if __name__ == "__main__":
    main()