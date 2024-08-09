import requests
from requests.auth import HTTPBasicAuth

# Prompt user for URL input
url = input("Enter the URL to test for admin login: ").strip()

# Open the file containing passwords
with open('passwords.txt') as passwords:
    # Iterate through each password in the file
    for password in passwords.readlines():
        password = password.strip()  # Remove leading/trailing whitespace

        # Send HTTP GET request with Basic Authentication
        try:
            req = requests.get(url, auth=HTTPBasicAuth('admin', password))
            
            if req.status_code == 401:
                print(f"Password '{password}' failed.")
            elif req.status_code == 200:
                print('Login successful, password:', password)
                break
            else:
                print(f"Error occurred with password '{password}', status code: {req.status_code}")
                break
        except requests.exceptions.RequestException as e:
            print(f"An error occurred with password '{password}': {e}")
