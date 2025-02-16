"""

This python script demonstrates how to get URL list

"""
import json
import requests
from  esa_credentials import *
from requests.auth import HTTPBasicAuth

# Disable certificate warnings (not recommended for production use)
requests.packages.urllib3.disable_warnings()

# System Parameters
port = "4431"

def main():
    """ Function for retrieving URL list from the ESA """
    print("Retrieving URL list from the Email Security Appliance...")
    url = f"https://{esa_hostname}:{port}/esa/api/v2.0/config/url_lists?device_type=esa"
    try:
        response = requests.get(url, auth=HTTPBasicAuth(esa_username, esa_password), verify=False)
        # Check bad responses
        if response.status_code >= 200 and response.status_code < 300:
            print(json.dumps(response.json(), indent=4))  
        else:
            print(json.dumps(response.json(), indent=4))
            exit()
    except Exception as err:
        print("Error fetching info from ESA: " + str(err))
    return response


# MAIN function 
if __name__ == "__main__":
    main()
