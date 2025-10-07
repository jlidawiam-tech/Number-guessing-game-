from ast import For
import random
secret=random.randint(1,100)
t=int(0)
n=int
print("You Have 3 chances ")
while secret!=n and t<3:
    n=int(input("Guess a number:"))
    t+=1
    if n>secret:
        print("Too hight")
    elif n<secret:
        print("Too low")
    else:
        print("Correct.")
print("You failed, Try again")
