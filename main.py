# Flow of Program
# Uses subfinder to store subdomains in a Server.csv file
# Use request to get the following subdomain, url, status_code, title, server, content_type, final_url
# lastly display them fabulously.

import requests
from bs4 import BeautifulSoup

subdomain_file_name = "subdomain_raw.txt"
server_file_name = "Server.csv"

with open(subdomain_file_name, 'r') as file:
    content = file.read().splitlines()
    print("Requesting HTTP")
    for c in content:
        try:
            response = requests.get(f"https://{c}", timeout=5)
            response.raise_for_status()
            print("-----")
            print(f"Requesting {c}")
            print(f"subdomain : {c}")
            print(f" URL : {response.url}")
            soup = BeautifulSoup(response.text, "html.parser")
            if soup.title:
                print(f"title : {soup.title}")
            print(f"server : {response.headers.get("Server")}")
            print(f"content_type : {response.headers.get("Content-Type")}")
            print("-----")
    
        except requests.exceptions.RequestException as e:
            print("Failed")
            continue
    


