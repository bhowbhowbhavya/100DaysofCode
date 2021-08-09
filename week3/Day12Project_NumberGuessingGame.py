import sys
from random import randint
value = randint(1,100)
print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 to 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == "easy":
    d=9
else:
    d=4
def check_guess():
        for i in range(d,-1, -1):
            guessed_value=int(input("Make a guess: "))
            if guessed_value>value:
                print ("Too high.")
                print(f"You have {i} attempts remaining to guess the number. ")
            elif guessed_value<value:
                print("Too low.")
                print(f"You have {i} attempts remaining to guess the number. ")
            else: 
                print("Your guess is right!")
                sys.exit(0)
            if i==0:
                sys.exit(0)
        return 0
def guess():
    global difficulty
    global value
    if difficulty == "hard":
        print("You have 5 attempts to guess the number.")
        check_guess()        
    elif difficulty == "easy":
        print("You have 10 attempts to guess the number.")
        check_guess()
    else:
        print("Invalid diffivulty level.")
                   
guess()
                    

           
         
   
            
        


