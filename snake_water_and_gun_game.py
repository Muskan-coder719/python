import random

def GameWin(comp,you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True 
    elif comp=='g':
        if you=='s':
            return False 
        elif you=='s':
            return True
    
print( "Comp turn :snake(s),water(w) or gun(g):")
randNo=random.randint(1,3)
if randNo==1 :
    comp='s'
elif randNo==2:
    comp='w'
elif randNo=='g':
    comp='g'

you=input("Your turn : snake(s),water(w) or gun(g):")
a=GameWin(comp,you)

print("computer chose ",comp)
print("you chose",you)

if a==None :
    print("the game is a tie ")
elif a:
    print("You Win !")
else:
    print("You Lose")
