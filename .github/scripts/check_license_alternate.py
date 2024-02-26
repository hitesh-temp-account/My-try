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

    # Get list of files for the current key
    files = subprocess.check_output(["find", ".", "-type", "f", "-name", key]).decode().splitlines()

    # Get the value for the current key
    value = content[key]

    # Get list of excluded files matching the ignored paths
    excluded_files = []
    for path in excluded_paths:
        excluded_files.extend(subprocess.check_output(["find", ".", "-type", "f", "-name", key, "-path", path]).decode().splitlines())

    # Iterate over each file for the current key
    for file in files:
        # Check if the file is in the excluded files list
        if file in excluded_files:
            continue

        # Read the content of the file
        with open(file, 'r') as f:
            file_content = f.read()

            # Check if the value is present in the file content
            if value in file_content:
                print(f"{file} ... {GREEN}ok{RESET}")
            else:
                has_files_without_license = True
                print(f"{file} {RED}missing copyright!{RESET}")

# If there are files without a license, fail the script
if has_files_without_license:
    print("Failing this script as there is at least one file present without a license.")
    exit(1)
