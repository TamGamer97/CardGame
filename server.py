import socket
import time
import random
import cards
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host=socket.gethostname()
port = 6000

port = input("Create Code ")
port = int(port)

print("NAME:" ,host)
print("CODE:" ,port)

s.bind((host,port))
s.listen(2)
con,addr=s.accept()
conName = con.recv(1024).decode()
print(conName, "has joined the game")


def asignRoles():

    recieveMsg = "You can recieve now"
    con.send(str(recieveMsg).encode())
    con2.send(str(recieveMsg).encode())

    val1 = cards.value
    val2 = cards.value2

    number = cards.CardsAmount
    numbero = 0

    if("imposter" in cards.value and "imposter" in cards.value2):
        val1 = random.sample(cards.cadsPack, k=cards.CardsAmount)
        val2 = random.sample(cards.cadsPack, k=cards.CardsAmount)
        print("Cards changed because two many imposters")


    for card in cards.value and cards.value2:
        if card != "imposter":
            numbero += 1
            res = number - numbero
            print("this is res ", res)
            # if res is == 0 its not there
            # anything else it is there
            if res == 0:
                val1 = cards.value4
                val2 = cards.value5
                print("Cards changed because no imposter")




    messg = val1
    con.send(str(messg).encode())

    messg2 = val2
    con2.send(str(messg2).encode())

    if("imposter" in val1):
        print(conName, "is the imposter")
        PlayerImposter = con

    if("imposter" in val2):
        print(Con2Name, "is the imposter")
        PlayerImposter = con2

while True:
    con2,addr=s.accept()
    Con2Name = con2.recv(1024).decode()
    str(Con2Name)
    #print("Connected with ", addr, Con2Name)
    print(Con2Name, "has joined the game")
    ready = input("start? ")
    if(ready == "start"):
        asignRoles()
    if(ready != "start"):
        asignRoles()
    break

input("") #exit