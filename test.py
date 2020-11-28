import cards
import socket


number = 6
numbero = 0


for card in cards.value:
    if card != "imposter":
        numbero += 1
        res = number - numbero
        #print("this is res ", res)
        # if res is == 0 its not there
        # anything else it is there


Hello = ["one", "two", "three", "imposter"]
#print(type(Hello))
Hello = str(Hello)


Hello = Hello.replace("[", "")
Hello = Hello.replace("]", "")
Hello = Hello.replace("'", "")
#print(Hello)
#print(type(Hello))


Hello = Hello.split(", ")
#print(Hello)
#print(type(Hello))


if("one" in Hello):
    #print("yes")
    pass
else:
    #print("No")
    pass

Myname = socket.gethostname()

#print("MyName is ", type(Myname))




card = input("?")


