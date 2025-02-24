import subprocess
import ctypes
import sys

def is_admin():
    """Check if the script is running with administrative privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def stop_iis_site(site_name):
    try:
        # PowerShell command to stop the specific site
        powershell_command = f"Stop-Website -Name '{site_name}'"
        
        # Run the PowerShell command
        result = subprocess.run(
            ["powershell", "-Command", powershell_command],
            check=True,
            text=True,
            capture_output=True
        )
        
        # Print the output
        print(f"Site '{site_name}' stopped successfully:")
        print(result.stdout)
    
    except subprocess.CalledProcessError as e:
        print(f"Failed to stop the site: {e}")
        print(e.stderr)

# Check if the script is running as admin
if not is_admin():
    # Re-run the script with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
else:
    # Example usage
    site_name = "Hallmark"  # Replace with your site name
    stop_iis_site(site_name)