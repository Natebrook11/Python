from tkinter import Scale
import pyqrcode
import io

link = input("Url:")
name = input("Name of the qr:")
url = pyqrcode.create(link)

url.svg(name + ".svg" , scale=10)
buffer = io.BytesIO()
url.svg(buffer)
print("Done!")