import os
import json
import subprocess

# Read content from .licenserc.json
with open('.licenserc.json', 'r') as f:
    content = json.load(f)

# Define color codes
RED = '\033[0;31m'
GREEN = '\033[0;32m'
RESET = '\033[0m'

# Initialize an empty list to store the keys
keys = list(content.keys())

# Initialize a variable to keep track of whether there are files without a license
has_files_without_license = False

# Read the list of excluded paths from the JSON content
excluded_paths = content.get('ignore', [])

# Iterate over each type of file and check for the presence of license
for key in keys:
    # Don't consider 'ignore' key for license checking
    if key == "ignore":
        continue

    # Construct the find command with excluded paths
    find_command = ["find", ".", "-type", "f", "-name", key]
    for path in excluded_paths:
        find_command.extend(["-not", "-path", path])

    # Execute the find command
    files = subprocess.check_output(find_command).decode().splitlines()

    value = content[key]
    print(f"key: {key}")
    print(f"value: {value}")
    for file in files:
        with open(file, 'r') as f:
            file_content = f.read()
            if value in file_content:
                print(f"{file} ... {GREEN}ok{RESET}")
            else:
                has_files_without_license = True
                print(f"{file} {RED}missing copyright!{RESET}")

# If there are files without a license, fail the script
if has_files_without_license:
    print("Failing this script as there is at least one file present without a license.")
    exit(1)
