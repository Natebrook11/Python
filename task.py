from tkinter import *
from tkinter.ttk import *
import datetime

x = datetime.datetime.now()
print(x)

def show():
    print("Show on")
    root = Tk()
    root.title("TaskCenter By Nate Brook")
    file = open('task.txt', 'r')
    string = file.read()
    file.close()
    label = Label(root, font=("ds-digital", 30), background="black", foreground="white")
    label.pack(anchor="center")
    label.config(text=string)




def add():
    name = input('Task Name: ')
    pwd = input("Body: ")
    file = open('task.txt', 'a')
    file.write(name + "|" + pwd + "\n")
    file.close()
    print("Task added")

def detele():
    print("Task deteled")
    file_detele = open('task.txt' , 'w')
    file_detele.close()


while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add, detele), press q to quit? ").lower()
    if mode == "q":
        break
    if mode == "add":
        add()
    if mode == "view":
        show()
    elif mode == "detele":
        detele()
    else:
        print("Invalid mode.")
        continue
