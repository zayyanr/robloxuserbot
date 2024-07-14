import requests

# Do not change (endpoint)
ROBLOX_API_URL = 'https://users.roblox.com/v1/usernames/users'

# Name you want to check
name = input("Username: ") 

# Function to check if a username is already registered on Roblox
def is_username_registered(username):
    headers = {'Content-Type': 'application/json'}
    data = {'usernames': [username]}

    try:
        response = requests.post(ROBLOX_API_URL, headers=headers, json=data)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        return None

    if response.status_code == 200:
        data = response.json()
        # Check if the username is in the list of taken usernames
        return username.lower() in [user['name'].lower() for user in data['data']]
    else:
        # Handle other status codes as needed
        print(f"Unexpected status code: {response.status_code}")
        return None

# Check if the username is taken and print the result
is_taken = is_username_registered(name)
if is_taken is None:
    print("There was an error checking the username.")
elif is_taken:
    print(f"The username '{name}' is already taken.")
else:
    print(f"The username '{name}' is available.")
