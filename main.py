#M.Sython
#Rock,Paper,scissors
#update 2.1.1 : colors
import random #import for PC move

class color : 
   green = '\033[92m'
   red = '\033[91m'
   white = '\033[0m'
   yellow = '\033[93m'
   blue = '\033[94m'
   porple = '\033[95m'
   gray = '\033[90m'

print(color.green + "welcome " + color.white + "to " + color.red + "game")
print(color.white + 'rock = 1')
print('paper = 2')
print('scissors = 3')
print(color.red + "exit = 0")

print(color.yellow + "select your mode")
print(color.blue + "p for pvp")
print(color.porple + "e for pve")
gm=input() #input gamemode from user

p1w = 0 #player 1 points
p2w = 0 #player 2 points
while p1w < 3 and p2w < 3:   #check earn 3 point
    print(f"{color.yellow} p1 wins: {p1w} and p2 wins : {p2w}") #show points
    p1=input(color.blue + "p1 move : ")
    if gm == "p": #check gamemode
        p2=input(color.porple + "p2 move :")
    #check who is winner :
    elif gm == "e":
        p2=random.randint(1, 3)
        print(f"{color.porple}system move is {p2}")
    try:
        p1=int(p1)
        p2=int(p2)
    except:
        print(color.red + "your move is wrong")
        break
    if p1 == 0:
        print(color.red + "p1 left")
        print(color.porple + "p2 is final winner")
        p1w = 3
        p2w = 0
        break
    elif p2 == 0:
        print(color.red + "p2 left")
        print(color.blue + "p1 is final winner")
        p1w = 0
        p2w = 3
        break
    if p1 == 1 and p2 == 3:
        print(color.blue + "p1 winner")
        p1w = p1w + 1
    elif p1 == 1 and p2 == 2:
        print(color.porple + "p2 winner")
        p2w = p2w + 1
    elif p1 == p2:
        print(color.yellow + 'equal')
    elif p1 == 2 and p2 == 1:
        print(color.blue + "p1 winner")
        p1w = p1w + 1
    elif p1 == 2 and p2 == 3:
        print(color.porple + "p2 winner")
        p2w = p2w + 1
    elif p1 == 3 and p2 == 1:
        print(color.porple + "p2 winner")
        p2w = p2w + 1
    elif p1 == 3 and p2 == 2:
        print(color.blue + "p1 winner")
        p1w = p1w + 1
    else:
        print(color.red + "your move is wrong")
print(color.yellow + "game has ended")
print(f"{color.yellow} p1 final points: {p1w} and p2 points: {p2w}")
