import random
a= int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors"))
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

if a==0:
    print(rock)  
elif a ==1:
    print(paper)  
else:
    print(scissors)
print("Computer chose")
mylist = [rock, paper, scissors]
b = random.choice(mylist)
print(b)

if a>=3 or a <0:
    print("Invalid")
else:
    if a==0:
        if b==rock:
            print("Draw")
        elif b==paper:
            print("You lose!")
        else:
            print("You won!")
    if a==1:
        if b==rock:
            print("You won")
        elif b==paper:
            print("Draw")
        else:
            print("You lose!")
    if a==2:
        if b==rock:
            print("You lose!")
        elif b==paper:
            print("You won!")
        else:
            print("Draw!")