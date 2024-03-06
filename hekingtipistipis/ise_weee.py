import requests

# Function to attempt to restore a Facebook account using phone number
def restore_facebook_account_with_phone(email, password):
    # Define the URL for the login page
    login_url = 'https://www.facebook.com/login/identify?ctx=recover'
    
    # Define the payload with the phone number and password
    payload = {
        'email': email,
        'password': password
    }
    
    # Send a POST request to the login page
    response = requests.post(login_url, data=payload)
    
    # Check if the response contains a successful login attempt
    if "Log in to Facebook" in response.text:
        print("Failed to restore the account.")
    else:
        print("Account restored successfully!")

# Example usage:
restore_facebook_account_with_phone('kucingbadut5@gmail.com', 'karpetandongku')