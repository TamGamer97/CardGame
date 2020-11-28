import socket
import time
import cards
from tkinter import *
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


username = "defualt"
host = ""
port = 0

def GamePage():
    Game = Toplevel()
    



def joinGame():
    global username
    global host
    global port
    username = usernameInput.get()
    host = hostInput.get()
    port = portInput.get()
    username = str(username)
    host = str(host)
    port = int(port)
    print(username, host, port)
    s.connect((host, port))
    myName = s.send(username.encode())
    wp = Toplevel(root)
    lb1 = Label(wp, text="Waiting for " + host + " to start")
    lb1.pack()
    if(s.recv(1024)):
        print("Game Started")



root = Tk()
root.geometry("1300x600")


usernameInput = Entry(root)
usernameInput.insert(0, "username")

hostInput = Entry(root)
hostInput.insert(0, "host name")


portInput = Entry(root)
portInput.insert(0, "code")

btnJoin = Button(root, text="Join Game", command=joinGame)

usernameInput.pack()
hostInput.pack()
portInput.pack()
btnJoin.pack()


root.mainloop()














#always = s.recv(1024).decode()

#always = input("Recieve ")


def usedCard(card):
    #pass in correct card
    print(card)
    #check if card is in list
    if(card in cardsList):
        #update list
        cardsList.remove(card)

    print("")
    print(cardsList)
    useCards(cardsList)

def useCards(cardsList):
    card = input("use a card ")
    if(card == "life"):
        if("life" in cardsList):
            print("ok using life")
            usedCard(card)
        else:
            print("no Life")
            useCards(cardsList)

    if(card == "imposter"):
        if("imposter" in cardsList):
            print("ok using Imposter")
            usedCard(card)

        else:
            print("no imposter")
            useCards(cardsList)

    if(card == "king"):
        if("king" in cardsList):
            print("ok using king")  
            usedCard(card)
        else:
            print("no king")
            useCards(cardsList)

    if(card == "queen"):
        if("queen" in cardsList):
            print("ok using queen")  
            usedCard(card)
        else:
            print("no queen")
            useCards(cardsList)

    if(card == "joker"):
        if("joker" in cardsList):
            print("ok using joker")  
            usedCard(card)
        else:
            print("no joker")
            useCards(cardsList)

    
    if(card == "jack"):
        if("jack" in cardsList):
            print("ok using jack")
            usedCard(card)
        else:
            print("no jack")
            useCards(cardsList)
    
    if(card == "list" or card == "cards" or card == "card"):
        print(cardsList)

    if(card == "quit" or card == "quit"):
        input("Thanks for playing")
        quit()

    if(card != "jack" or card != "joker" or card != "queen" or card != "king" or card != "imposter" or card != "life" or card != "list" or card != "cards" or card != "card" or card != "quit" or card != "exit"):
        print("card does not exist")
        useCards(cardsList)

if s.recv(1024):
    cards = s.recv(1024)
    cards = cards.decode()
    print(" ")
    cards = cards.replace("[", "")
    cards = cards.replace("]", "")
    cards = cards.replace("'", "")
    cardsList = cards.split(", ")
    print("cards:", cards)

    if("imposter" in cardsList):
        print("YOURE IMPOSTER")
    
    useCards(cardsList)



    #turn card str into list so you can take away cards

#]if(s_messg.decode() == "I"):
   #print("YOUR IMPOSTER")

#if(s_messg.decode() != "I"):
    #print("innocent")
input() #end



























