import iis_bridge.pool as pool

# Define variables
client_name = "Hallmark"
date = "24022025"
app_pool_name = f"{client_name}_{date}"

# Check if the application pool exists
if not pool.exists(app_pool_name):
    # Create a new application pool
    pool.create(app_pool_name)
    print(f"Application Pool {app_pool_name} created successfully.")
else:
    print(f"Application Pool {app_pool_name} already exists.")

# Configure advanced settings
try:
    # Enable 32-bit applications
    pool.config(app_pool_name, thirty_two_bit=True)

    # Set idle timeout to 1440 minutes (24 hours) in the correct format (hh:mm:ss)
    pool.config(app_pool_name, idle_timeout="24:00:00")

    # Disable periodic restart (set to 0 minutes)
    pool.config(app_pool_name, recycle_after_time="00:00:00")

    # Set specific recycling time to 02:00 AM
    pool.config(app_pool_name, recycle_at_time="02:00:00")

    print(f"Application Pool {app_pool_name} configured successfully.")
except Exception as e:
    print(f"An error occurred while configuring the application pool: {e}")