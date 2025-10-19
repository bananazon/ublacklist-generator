#!/usr/bin/env python3

from pathlib import Path
from pprint import pprint
import urllib.error
import urllib.parse
import urllib.request
import json
import signal
import socket
import sys

def handle_sigint(signum, frame):
    print(f'\nCaught Ctrl+C (signal {signum})')
    sys.exit(0)

def domain_resolves(domain):
    print(f'Testing domain {domain}')
    try:
        socket.gethostbyname(domain)
        return True
    except socket.gaierror:
        return False

signal.signal(signal.SIGINT, handle_sigint)

def get_country_domains():
    url = 'https://raw.githubusercontent.com/samayo/country-json/refs/heads/master/src/country-by-domain-tld.json'
    headers = {
        'Accept': 'application/json',
    }

    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=5) as response:
        raw_body = response.read().decode('utf-8').strip()
        try:
            json_data = json.loads(raw_body)
        except Exception as e:
            print(f'Error: {e}')
            sys.exit(1)

    return json_data

def main():
    domain = 'pinterest'
    common_tlds = ['.com', '.edu', '.net', '.org']
    to_check = []
    block_list = []
    
    for tld in common_tlds:
        to_check.append(f'{domain}{tld}')

    json_data = get_country_domains()

    for country in json_data:
        if 'tld' in country and country['tld'] is not None:
            tld = country['tld']
            to_check.append(f'{domain}{tld}')

    for item in to_check:
        if domain_resolves(item):
            block_list.append(f'*://*.{item}/*')

    for entry in sorted(block_list):
        print(entry)

if __name__ == '__main__':
    main()
