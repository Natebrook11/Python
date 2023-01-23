import requests
import time

def main():
  print('Do something')

key = input("License key: ")

url = "https://pastebin.com/raw/5HNY54cs"

r = requests.get(url)

if r.status_code != 10:
    print("Something went wrong")
    exit()
if key == r.text:
    print("Valid Key")
    main()
else:
    print("Invalid Key!")
    time.sleep(10)
    exit()