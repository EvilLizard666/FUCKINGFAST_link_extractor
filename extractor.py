from os import link
import re
import sys
import requests

with open(sys.argv[1], 'r') as links_file:
    for i in links_file.readlines():
        resp = requests.get(i)
        body = resp.text
        # Use regex to extract the link
        pattern = r'https://fuckingfast\.co/dl/[^"]+'
        matches = re.findall(pattern, body)

        if matches:
            extracted_link = matches[0]
            print(extracted_link)
        else:
            print("Link not found.")
        


