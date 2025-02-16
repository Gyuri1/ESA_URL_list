# ESA_URL_list



These script show how to use Email Security Appliance (ESA)  API.


How to install:
====
To install and set up the script, follow these steps:  
  1.	Clone the repository to your local machine: ```git clone https://github.com/Gyuri1/ESA_URL_list```  
  2.	Navigate to the project directory: ```cd ESA_URL_list```
  3.	Ensure you have Python 3 installed. You can check your Python version with: ```python3 --version```
  4.	Please install ```requests``` package using ```pip```: ```pip install requests```
  5.	Please update ```esa_credentials.py``` with Your ESA credentials!
  6.	Please check the port = "4431" as an API port for ESA in the python scripts!

How to run:
====

Show URL list from ESA

    python3 esa_url_list.py


Expected Output: 
====

After running the script, you should see similar output:  

   ```sh
python3 esa_url_list.py
Retrieving URL list from the Email Security Appliance...
{
    "data": [
        {
            "used_by": "",
            "urls_count": 1,
            "name": "test",
            "urls": [
                "a1.com"
            ]
        }
    ]
}

 ```

How to run the POST request:
====

Add a new URL list to ESA:

    python3 esa_post_url_list.py -f test.json

where ```-f``` is the mandatory argument for the JSON format filename. 


Expected Output: 
====

After running the script, you should see similar output: 

   ```sh
python3 esa_post_url_list.py -f test.json
Reading JSON file...
URL List Name: test
Sending URL list to Email Security Appliance...
url: https://esa.company.com:4431/esa/api/v2.0/config/url_lists/test?device_type=esa
response.status_code: 201
Good request: {
    "data": {
        "message": "Added Successfully"
    }
}

 ```


This picture shows the uploaded URL List on ESA GUI:

![Alt text](esa-gui.png?raw=true "ESA GUI with the URL List")



Comment:
- ESA API POST request requires the correct  Content-Type header! 


Reference:
https://www.cisco.com/c/en/us/td/docs/security/esa/esa15-0/api_guide/b_Secure_Email_API_Guide_15-0/b_ESA_API_Guide_chapter_010.html#Cisco_Concept.dita_3cc91316-6b13-4d8a-ad88-d97847ed65cc

