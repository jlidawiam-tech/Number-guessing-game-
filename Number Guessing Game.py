import random
secret=random.randint(1,100)
t=int(0)
n=int
while secret!=n:
    n=int(input("Guess a number:"))
    t=t+1
    if n>secret:
        print("Too hight")
    elif n<secret:
        print("Too low")
    else:
        print("Correct.")
print("You tried",t,"times")
