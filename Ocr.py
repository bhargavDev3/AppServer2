import re

# Define the client name and site
client_name = "pink"
client_site = f"https://{client_name}.nimbleproperty.net"

# Define the paths to the OCR files
OCR_management = r"C:\Production2\Hallmark\Build\OCR\OCRManagement.js"
OCR_mapping = r"C:\Production2\Hallmark\Build\OCR\OCRFiles\Scripts\Mapping.js"

# Step 1: Replace the apiurl with the client_site (regardless of the current value)
def replace_apiurl(content):
    pattern = r"var apiurl = '[^']*';"
    replacement = f"var apiurl = '{client_site}/OCRWEBAPI/api';"
    return re.sub(pattern, replacement, content)

# Step 2: Replace the host with the client_site (regardless of the current value)
def replace_host(content):
    pattern = r"var host = '[^']*';"
    replacement = f"var host = '{client_site}';"
    return re.sub(pattern, replacement, content)

# Function to process a file
def process_file(file_path):
    # Read the content of the file
    with open(file_path, 'r') as file:
        content = file.read()

    # Perform the replacements
    content = replace_apiurl(content)
    content = replace_host(content)

    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.write(content)

    print(f"File '{file_path}' has been updated successfully.")

# Process both files
process_file(OCR_management)
process_file(OCR_mapping)