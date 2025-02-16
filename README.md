# ESA_URL_list



These script show how to use Email Security Appliance (ESA)  API.


How to install:
====
To install and set up the script, follow these steps:  
	1.	Clone the repository to your local machine: ```git clone https://github.com/Gyuri1/ESA_URL_list```  
	2.	Navigate to the project directory: ```cd ESA_URL_list```  
 	3.	Ensure you have Python 3 installed. You can check your Python version with: ```python3 --version```  
  4.  Please install ```requests``` package using ```pip```: ```pip install requests```  
  5.  Please update ```esa_credentials.py``` with Your ESA credentials! 

How to run:
====

1. Show URL list from ESA

    python3 esa_url_list.py


Expected Output: 
====

After running the script, you should obtain a CSV file named firewall-rules.csv containing the generated firewall rules.  

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
