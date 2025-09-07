import datetime
import os

# Get the absolute path of the current script's parent folder
parent_folder = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(parent_folder, "output.txt")

# Open the file in append mode ('a') so it creates the file if it doesn't exist, or appends if it does
with open(output_path, "a") as f:
    f.write("This is a sample line.\n")
    f.write(f"Timestamp: {datetime.datetime.now()}\n")
    f.write("=====\n")
