#M.Sython
import random #import for PC move


print("welcome to game")
print('rock = 1')
print('paper = 2')
print('scissors = 3')
print("exit = 0")


print("select your mode")
print("p for pvp")
print("e for pve")
gm=input() #input gamemode from user

p1w = 0 #player 1 points
p2w = 0 #player 2 points
while p1w < 3 and p2w < 3:   #check earn 3 point
    print(f"p1 wins: {p1w} and p2 wins : {p2w}") #show points
    p1=input("p1 move : ")
    if gm == "p": #check gamemode
        p2=input("player 2 move :")
    #check who is winner :
    elif gm == "e":
        p2=random.randint(1, 3)
        print(f"system move is {p2}")
    p1=int(p1)
    p2=int(p2)
    if p1 == 0:
        print("p1 exit the game")
        print("p2 is final winner")
        p1w = 3
        p2w = 0
        break
    elif p2 == 0:
        print("p2 enseraf dad")
        print("p1 barande nahaii ast")
        p1w = 0
        p2w = 3
        break
    if p1 == 1 and p2 == 3:
        print("p1 winner")
        p1w = p1w + 1
    elif p1 == 1 and p2 == 2:
        print("p2 winner")
        p2w = p2w + 1
    elif p1 == p2:
        print('equal')
    elif p1 == 2 and p2 == 1:
        print("p1 winner")
        p1w = p1w + 1
    elif p1 == 2 and p2 == 3:
        print("p2 winner")
        p2w = p2w + 1
    elif p1 == 3 and p2 == 1:
        print("p2 winner")
        p2w = p2w + 1
    elif p1 == 3 and p2 == 2:
        print("p1 winner")
        p1w = p1w + 1
    else:
        print("vorodi shoma ghlat mibashad")
print("game has ended")
print(f"p1 final points: {p1w} and p2 points: {p2w}")
