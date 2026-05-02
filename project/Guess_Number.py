import random

n= random.randint(1,50)
a=0
guess=0
while(a!=n):
    guess=guess+1
    a=int(input("Guess the number: "))
    if(a>n):
         print("Guess Lower Number Please!!")
    else:
        print("Guess Higher Number Please!!") 

print(f"Congratulations!!You have guessed the number {n} in {guess} attemps.")