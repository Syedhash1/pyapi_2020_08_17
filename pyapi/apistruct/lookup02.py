#!/usr/bin/env python3
import requests

import argparse

def main():
  mytoken = '4182163ba3dd50b0dccfd102982f0b9a3a9d27c47bdca8df'
  myapi = "https://fonoapi.freshpixl.com/v1/getlatest"
  mybuiltapi = myapi + "?token=" + mytoken
  parser.addargument("manu", help="Get the manufacture name")
  
  args = parser.parse_args()
  print(args.manu)

  ## ask user for a brand to search on
 # brand = input("What brand of device are you searching for?")
  brand =  args.manu
  
  ## translate our JSON response to a series of Python lists and dictionaries
  myjson = requests.get(mybuiltapi + "&brand=" + brand).json()
  
  ## Display a list of what inside our JSON
  for x in myjson:
    print(x)


if __name__ == '__main__':
  main()

