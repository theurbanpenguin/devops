import os
import subprocess
from datetime import datetime

# Configuration
local_directory = "/home/vagrant/data"
backup_name = f"backup_{datetime.now().strftime('%Y%m%d_')}.tar.gz"

# Create a tarball of the local directory
subprocess.run(["tar", "-czf", backup_name, "-C", local_directory, "."])

print("Backup completed successfully.")
