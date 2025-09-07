# Read and print the contents of output.txt from the same folder as this script
import os

parent_folder = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(parent_folder, "output.txt")

with open(output_path, "r") as f:
    content = f.read()
    print(content)
