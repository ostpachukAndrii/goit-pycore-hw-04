import os
import sys
from colorama import Fore, Style, init

init(autoreset=True)  # Initialize colorama


def print_folder_structure(root_path, indent=0):
    if not os.path.exists(root_path):
        print(Fore.RED + f"Path '{root_path}' does not exist.")
        return

    for item in os.listdir(root_path):
        path = os.path.join(root_path, item)
        if os.path.isdir(path):
            print(" " * indent + Fore.BLUE + f"{item}")
            print_folder_structure(path, indent + 2)
        else:
            print(" " * indent + Fore.GREEN + f"{item}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(Fore.RED + "Please provide a folder path.\nUsage: python file-colorama.py <folder_path>")
    else:
        folder_path = sys.argv[1]
        print_folder_structure(folder_path)