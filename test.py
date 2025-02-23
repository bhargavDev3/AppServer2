import subprocess

site_name = "Hallmark"

# Step 1: Start W3SVC service if it's not running
start_w3svc = "net start W3SVC"
subprocess.run(start_w3svc, shell=True, capture_output=True, text=True)

# Step 2: Stop the IIS website
command = f'C:\\Windows\\System32\\inetsrv\\appcmd.exe stop site /site.name:"{site_name}"'

try:
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    print("STDOUT:", result.stdout)  # Print standard output
    print("STDERR:", result.stderr)  # Print error message

    if result.returncode == 0:
        print(f"Website '{site_name}' stopped successfully.")
    else:
        print(f"Failed to stop website '{site_name}'. Exit Code: {result.returncode}")
except Exception as e:
    print(f"An error occurred: {e}")