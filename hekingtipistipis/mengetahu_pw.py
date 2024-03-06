import os
import re

# Function to retrieve Wi-Fi passwords on a Windows machine
def get_wifi_passwords():
    # Use the 'netsh' command to list all Wi-Fi profiles
    profiles_data = os.popen('netsh wlan show profiles').read()
    # Use regular expression to find all Wi-Fi profile names
    profile_names = re.findall(r'All User Profile\s+:\s(.*)', profiles_data)
    
    # Dictionary to store Wi-Fi profiles and their passwords
    wifi_passwords = {}
    
    # For each profile, attempt to retrieve the password
    for name in profile_names:
        # Get the details of the profile
        profile_info = os.popen(f'netsh wlan show profile name="{name}" key=clear').read()
        # Use regular expression to find the password
        password = re.search(r'Key Content\s+:\s(.*)', profile_info)
        if password:
            # Add the password to the dictionary
            wifi_passwords[name] = password.group(1)
        else:
            # If password is not found, add None
            wifi_passwords[name] = None
    
    return wifi_passwords

# Example usage:
wifi_passwords = get_wifi_passwords()
print(wifi_passwords)