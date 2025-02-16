"""

This python script demonstrates how to get URL list

"""
import argparse
import json
import os
import requests
from  esa_credentials import *
from requests.auth import HTTPBasicAuth

# Disable certificate warnings (not recommended for production use)
requests.packages.urllib3.disable_warnings()

# System Parameters
port = "4431"

def main(filename):
    print("Reading JSON file...")
    try:
        # Open and read the JSON file
        with open(filename, 'r') as file:
            data = json.load(file)
            #print(data)
            url_list_name,ext = os.path.splitext(filename)
            print("URL List Name:",url_list_name)
            
    except Exception as err:
        print("Error reading from filename: " + str(err))
       
    headers = {'Content-Type': 'application/json'}

    print("Sending URL list to Email Security Appliance...")
    
    url = f"https://{esa_hostname}:{port}/esa/api/v2.0/config/url_lists/{url_list_name}?device_type=esa"
    try:
        # posting to ESA
        print("url:",url)
        response = requests.post(url, auth=HTTPBasicAuth(esa_username, esa_password), data = json.dumps(data), headers=headers, verify=False)
       
        print("response.status_code:", response.status_code)
        # Check bad responses
        if response.status_code >= 200 and response.status_code < 300:
            print("Good request:", json.dumps(response.json(), indent=4))  

        else:
            print("Bad request:",json.dumps(response.json(), indent=4))
            exit()
    except Exception as err:
        print("Error sending info to ESA: " + str(err))
    return 


# MAIN function 
if __name__ == "__main__":

    # Argument parser
    parser = argparse.ArgumentParser(
        description="This script shows how to send URL List to ESA"
    )
    parser.add_argument("-f", help="JSON filename", required=True)
    
    args = parser.parse_args()
    main(args.f)
