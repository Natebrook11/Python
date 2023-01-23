import requests
web = input("Image web link")
r = requests.get(web)

print(r.content)
with open("output.png" , "wb") as f:
    f.write(r.content)