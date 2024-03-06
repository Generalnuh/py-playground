import os
import re
import subprocess

# Function to detect nearby Wi-Fi networks and retrieve their passwords
def detect_wifi_networks_and_passwords():
    # Use the 'netsh' command to list all Wi-Fi profiles
    profiles_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], shell=True).decode('utf-8')
    # Use regular expression to find all Wi-Fi profile names
    profile_names = re.findall(r'All User Profile\s+:\s(.*)', profiles_data)
    
    # Dictionary to store Wi-Fi profiles and their passwords
    wifi_networks = {}
    
    # For each profile, attempt to retrieve the password
    for name in profile_names:
        # Remove any leading or trailing whitespace
        name = name.strip()
        # Get the details of the profile
        try:
            profile_info = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', name, 'key=clear'], shell=True).decode('utf-8')
            # Use regular expression to find the password
            password = re.search(r'Key Content\s+:\s(.*)', profile_info)
            if password:
                # Add the password to the dictionary
                wifi_networks[name] = password.group(1)
            else:
                # If password is not found, add None
                wifi_networks[name] = None
        except subprocess.CalledProcessError as e:
            # If there's an error retrieving the profile, add None
            wifi_networks[name] = None
    
    return wifi_networks

# Example usage:
wifi_networks = detect_wifi_networks_and_passwords()
print(wifi_networks)