import tweepy
from time import sleep
import tkinter as tk
from tkinter import *
import sys
import socket
from requests import get
import platform, socket, os
import itertools
import re

#Twitter

ckey = 'lZ4fMaxdDVxKR5K3d8uWouYQg'
csec = 'KHJQI9ItN6XsVwyPepjTt6nTfc9RPyyyPcZBAY0wGhZqvSUXEs'
ownid = 38600811
atoken = '38600811-NVnUljfAW1OW6CuTVtLWSNpfcCYElFeHvq0lO7kRT'
astoken = 'aq0cpLqQ6eUWXIy8jD0o2MNxMKq658IwWpoT5uJdghY0t'

auth = tweepy.OAuthHandler(ckey, csec)
auth.set_access_token(atoken, astoken)
auth.secure = True
api = tweepy.API(auth)
myBot = api.get_user(screen_name='shadowofanubis')

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        try:
            displayField.insert('1.0', "----------------------------------" + '\n')
            displayField.insert('1.0',(status.text + '\n' + '\n'))
            statuser.set("The length of the last tweet is: " + str(len(status.text)))
        except:
            pass

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_error disconnects the stream
            return False


# For Tkinter, you have to define a thing (status = Label(...)) and THEN you put that on the window (status.pack(...))

def getFieldText():
    displayField.delete("1.0", END)
    fieldText = entryField.get()
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
    searchTerm = "#" + entryField.get()
    myStream.filter(track=[searchTerm], async=True)
    print(searchTerm)
    return fieldText

def getFieldText2(nameoftrend):
    displayField.delete("1.0", END)
    fieldText = nameoftrend
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
    if fieldText.startswith("#"):
        searchTerm = fieldText
    else:
        searchTerm = "#" + fieldText
    print(searchTerm)
    myStream.filter(track=[searchTerm], async=True)
    return fieldText


# tkinter

root = Tk() #Blank window
root.resizable(0,1)
root.title("Tweasy")
root.grid_rowconfigure(0,weight=1)
root.grid_rowconfigure(1,weight=0)
root.grid_columnconfigure(0,weight=1)
root.grid_columnconfigure(1,weight=1)
root.grid_columnconfigure(2,weight=1)

leftFrame = Frame(root,bg="LightSteelBlue2")
leftFrame.grid(row=0, column=0, sticky="NS")
leftFrame.rowconfigure(3,weight=1)
rightFrame = Frame(root,bg="LightSteelBlue3")
rightFrame.grid(row=0, column=2, sticky="NS")
rightFrame.rowconfigure(0,weight=1)
bottomFrame = Frame(root, bg="LightSteelBlue4")
bottomFrame.grid(row=1, column=0,columnspan=3,sticky="WE")



labelentryField = Label(leftFrame, text="Hashtag Search Field", background="LightSteelBlue4", foreground="white")
labelentryField.grid(row=0, column=0,sticky=E)

entryField = Entry(leftFrame, bg="LightSteelBlue2")
entryField.grid(row=0, column=1,sticky=W)

hashButton = Button(leftFrame, text="Accept Hashtag", command=getFieldText, bg="LightSteelBlue4",foreground="white")
hashButton.grid(row=1, column=0,sticky=E)

# discButton = Button(leftFrame, text="Disconnect",bg="LightSteelBlue4",foreground="white")
# discButton.grid(row=1,column=1,sticky=W)

labelFrm = LabelFrame(leftFrame, bg="LightSteelBlue4",fg="white",labelanchor='n',text="Trending",width=10,height=400)
labelFrm.grid(row=3,column=0,columnspan=2, sticky=N+S+E+W)

api.trends_place(23424977)
d = api.trends_place(23424977)
reallist = d[0]['trends']

displayField = Text(rightFrame,bg="LightSteelBlue3",bd=1,wrap=WORD)
displayField.grid(row=0, column=0,sticky=N+S+W+E)

statuser = StringVar()
statuser.set("The length of the last tweet is :")
status = Label(bottomFrame, textvariable=statuser, bd=1, anchor=S,bg="LightSteelBlue4",fg="white")
status.grid(sticky="S")

for num, L in zip(range(10),reallist):
    labelFrm.rowconfigure(num,weight=1)
    Button(labelFrm,text=L['name'],bg="LightSteelBlue1",command=lambda L=L: getFieldText2(L['name'])).grid(row=num,column=0,columnspan=2,sticky=N+S+W+E,padx=110)





root.mainloop() #When you have a GUI, you need that window continuously on the screen until you close it out.

# /tkinter


