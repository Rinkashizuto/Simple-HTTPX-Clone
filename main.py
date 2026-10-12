# Flow of Program
# Uses subfinder to store subdomains in a Server.csv file
# Use request to get the following subdomain, url, status_code, title, server, content_type, final_url
# lastly display them fabulously.

import csv
import requests
from bs4 import BeautifulSoup

subdomain_file_name = "subdomain_raw.txt"
server_file_name = "Server.csv"

Fieldnames = ["subdomain",'url','status_code','title','server','content_type','final_url']

def check_host(subdomain):
    row = {
        "subdomain": subdomain,
        "url": f"https://{subdomain}",
        "status_code": "error",
        "title": "",
        "server": "",
        "content_type": "",
        "final_url": "",
    }

    try:
        r = requests.get(f"https://{subdomain}", timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")
        if soup.title and soup.title.string:
            row['title'] = soup.title.string.strip()

        else:
            row['title'] = "N/A"
        row['server'] = r.headers.get('Server', '')
        row['content_type'] = r.headers.get('Content-Type', '')
        row['final_url'] = r.url
        row['status_code'] = r.status_code


    except requests.exceptions.RequestException as e: 
        pass
    
    return row

with open(subdomain_file_name, 'r') as file:
    subdomains = list(set(file.read().splitlines()))
    
    print("Requesting HTTPS")
    results = [check_host(s) for s in subdomains]
        
with open(server_file_name, mode='w', newline='') as file:
    w = csv.DictWriter(file, fieldnames=Fieldnames)
    w.writeheader(Fieldnames)
    w.writerow(results)





