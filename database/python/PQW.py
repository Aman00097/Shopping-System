import random

r="rock"
p="paper"
s="scissor"
ch=''
while(ch==''):
    computer=random.choice([r,p,s])
    user=input("Enter choice:Rock, Paper or scissor or exit(C) \n").lower()
    if(user==computer):
        print("Tie")
    elif((user==p and computer==r) or (user==s and computer==p )or (user==r and computer==s )):
        print("You win")
    elif((user==p and computer==s) or (user==r and computer==p )or (user==s and computer== r)):
        print("You Loose")
    elif(user=='c'):
        ch=1
print(f"Computer choice is:{computer}")
