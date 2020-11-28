from tkinter import *
import client



root = Tk()

hostname = Entry(root)
hostname.insert(0, "Hostname")

username = Entry(root)
username.insert(0, "Your Name")

code = Entry(root)
code.insert(0, "Game code")

host = hostname.get()
port = code.get()

name = username.get()

def joinGame():
    print("joining Game")

FindBtn = Button(root, text="find lobby", command=joinGame)

username.pack()
hostname.pack()
code.pack()
FindBtn.pack()




root.mainloop()



