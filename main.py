import iis_bridge.pool as pool
import iis_bridge.site as site

# Define variables
client_name = "Hallmark"
date = "13022025"

app_pool_name = f"{client_name}_{date}"
site_name = client_name

try:
    # Check if the site exists
    if site.exists(site_name):
        print(f"Website '{site_name}' exists. Attempting to stop...")
        
        # Stop the site
        site.stop(site_name)
        print(f"Website '{site_name}' stopped successfully.")
    else:
        print(f"Website '{site_name}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")