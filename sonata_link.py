#!/usr/bin/env python3

import requests
import argparse

def fetch_archived_links(website, start_date=None, end_date=None):
    url = f"http://web.archive.org/cdx/search/cdx?url={website}//*&output=text&fl=original&collapse=urlkey"
    if start_date:
        url += f"&from={start_date}"
    if end_date:
        url += f"&to={end_date}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        links = response.text.splitlines()
        return links
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

def save_links_to_file(links, filename):
    try:
        with open(filename, 'w') as file:
            for link in links:
                file.write(f"{link}\n")
        print(f"Links have been saved to {filename}")
    except IOError as e:
        print(f"Error saving to file: {e}")

def main():
    parser = argparse.ArgumentParser(description="Fetch archived links from Wayback Machine")
    parser.add_argument("website", help="The website URL (e.g., example.com)")
    parser.add_argument("filename", help="The filename to save the links (e.g., links.txt)")
    parser.add_argument("--start-date", help="Start date for filtering (YYYYMMDD)")
    parser.add_argument("--end-date", help="End date for filtering (YYYYMMDD)")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    
    args = parser.parse_args()

    print("Fetching archived links...")
    links = fetch_archived_links(args.website, args.start_date, args.end_date)

    if args.verbose:
        print(f"Number of links found: {len(links)}")

    if links:
        save_links_to_file(links, args.filename)
    else:
        print("No links were found or there was an error.")

if __name__ == "__main__":
    main()
