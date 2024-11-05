"""Main Protocol Analyzer Module"""

from typing import Dict, List, Tuple
from protocols import PROTOCOLS

class ProtocolAnalyzer:
    def __init__(self):
        self.protocols = PROTOCOLS

    def analyze_function(self, function_name: str) -> Dict:
        """Analyze a function and return its details."""
        for protocol, categories in self.protocols.items():
            for category, functions in categories.items():
                if function_name in functions:
                    return {
                        'protocol': protocol,
                        'category': category,
                        'function': function_name,
                        'direction': functions[function_name]
                    }
        return {
            'protocol': 'UNKNOWN',
            'category': 'UNKNOWN',
            'function': function_name,
            'direction': 'UNKNOWN'
        }

    def list_protocols(self) -> None:
        """List all supported protocols and their functions."""
        for protocol, categories in self.protocols.items():
            print(f"\n{protocol}:")
            for category, functions in categories.items():
                print(f"\n  {category}:")
                for func, direction in functions.items():
                    print(f"    - {func}: {direction}")

def main():
    analyzer = ProtocolAnalyzer()
    
    while True:
        print("\nDeFi Protocol Analyzer")
        print("1. Analyze function")
        print("2. List all protocols")
        print("3. Exit")
        
        choice = input("\nChoice: ").strip()
        
        if choice == '1':
            func = input("Enter function name: ").strip()
            result = analyzer.analyze_function(func)
            print("\nAnalysis Result:")
            for key, value in result.items():
                print(f"{key}: {value}")
        
        elif choice == '2':
            analyzer.list_protocols()
        
        elif choice == '3':
            break

if __name__ == "__main__":
    main()