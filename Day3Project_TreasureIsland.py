print("Welcome to treasure island!\nYour mission is to find treasure.")
a= input("You're at a cross road.where do you want to go? Type 'left' or 'right'")
a=a.lower()
b= input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type'swim' to swim across")
b=b.lower()
c = input(" You arrive at an island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?")
c=c.lower()
d = "You enter a room of beasts. Game Over"
if a == "right":
    print(d)
else:
    if b == "swim":
        print(d)
    else:
        if c == "blue" or c == "red":
            print(d)
        else:
            print("You win!")
       

    
