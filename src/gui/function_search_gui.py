import tkinter as tk
from tkinter import ttk, scrolledtext
import os
import glob
import ast

class FunctionSearchGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("DeFi Function Search")
        self.root.geometry("800x600")

        # Input frame
        input_frame = ttk.Frame(root, padding="10")
        input_frame.pack(fill=tk.X)

        ttk.Label(input_frame, text="Enter functions (comma separated):").pack(side=tk.LEFT)
        self.function_input = ttk.Entry(input_frame, width=50)
        self.function_input.pack(side=tk.LEFT, padx=5)
        ttk.Button(input_frame, text="Search", command=self.search_functions).pack(side=tk.LEFT)

        # Results area
        self.results_area = scrolledtext.ScrolledText(root, width=90, height=30)
        self.results_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    def find_function_in_files(self, function_name):
        found_locations = []
        protocols_dir = "protocols"

        for root, dirs, files in os.walk(protocols_dir):
            for file in files:
                if file.endswith(".py") and not file.startswith("__"):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r') as f:
                            content = f.read()
                            if function_name in content:
                                # Get protocol name from path
                                protocol = os.path.basename(root)
                                if protocol == "protocols":
                                    protocol = os.path.splitext(file)[0]
                                found_locations.append(f"{protocol.upper()}")
                    except Exception as e:
                        continue

        return found_locations

    def search_functions(self):
        self.results_area.delete(1.0, tk.END)
        functions = [f.strip() for f in self.function_input.get().split(",")]

        for function in functions:
            if not function:
                continue

            locations = self.find_function_in_files(function)
            
            if locations:
                self.results_area.insert(tk.END, f"✅ '{function}' found in:\n")
                for loc in sorted(set(locations)):
                    self.results_area.insert(tk.END, f"   - {loc}\n")
            else:
                self.results_area.insert(tk.END, f"❌ '{function}' not found in any protocol\n")
            
            self.results_area.insert(tk.END, "\n")

def main():
    root = tk.Tk()
    app = FunctionSearchGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()