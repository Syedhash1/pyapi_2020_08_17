#!/usr/bin/env python3
"""
RZFeeser || Alta3 Research
Using regular expression to parse HTTPS responses
"""

import requests
import re

def main():
    # prompt user for "url" and "searchFor"
    print(f"Welcome to the simple HTTP response parser. Where should we search (ex: https://alta3.com)?")
    url = input()
    print(f"Great! So we'll try to open this url {url} to search for the phrase:")
    searchFor = input()

    # send an HTTP GET to the "url", then strip off the attached HTML data
    searchMe = requests.get(url).text


    def countoverlappingdistinct(searchFor, searchMe):
        total = 0
        start = 0
        there = re.compile(searchFor)

        while True:
          mo = there.search(searchMe, start)
          if mo is None: return total
          total += 1
          start = 1 + mo.start()
        print(total)



if __name__ == "__main__":
    main()

