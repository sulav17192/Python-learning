import random
play= "y"
while play=="y":
    computer= random.choice(["s", "w", "g"])

    Mystr=input("Enter Your Choice: ")
    FullForm = {"s": "Snake", "w": "Water", "g": "Gun"}
    MyChoice= Mystr

    try:
        print(f"You chose {FullForm[MyChoice]} \nComputer chose {FullForm[computer]}")
        if(computer==MyChoice):
            print("It's a Draw")
        else:
            if(computer=="s" and MyChoice=="w"):
                print("Computer won!!")
            
            elif(computer=="s" and MyChoice=="g"):
                print("You Won!!")

            elif(computer=="w" and MyChoice=="s"):
                print("You Won!!")

            elif(computer=="w" and MyChoice=="g"):
                print("Computer Won!!")

            elif(computer=="g" and MyChoice=="s"):
                print("Computer Won!!")

            elif(computer=="g" and MyChoice=="w"):
                print("You Won!!")
            else:
                print("Something went wrong")

    except KeyError:
        print("Invalid input. Try entering 's','w',or 'g'.") 

    play=input("Do you want to play again? (y/n): ")  

print("Thank You")    