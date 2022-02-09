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
import random
import time
comp = random.randint(1,3)
list = [rock,paper,scissors]
game_names = ["Rock","Paper","Scissors"]
players_choice = int(input("Enter Your Choice For This Game:\nPress 1: For Rock\nPress 2 : For Paper\nPress 3 : For Scissor\n"))
for i in range(1):
    print(rock)
    time.sleep(0.8)
    print(paper)
    time.sleep(0.8)
    print(scissors)
    time.sleep(0.8)

if comp ==1 and players_choice ==2:
    print(f"{list[comp-1]} Congratulation You Won Computer Choose {game_names[comp-1]}.")
elif comp==2 and players_choice==1:
    print(f"{list[comp-1]} Computer Won Because it Choose {game_names[comp-1]}.")
elif(comp==2 and players_choice==3):
    print(f"{list[comp-1]} Congratulation You Won Computer Choose {game_names[comp-1]}.")
elif(comp==3 and players_choice==2):
    print(f"{list[comp-1]} Computer Won Because it Choose {game_names[comp-1]}.")
elif(comp==1 and players_choice==3):
    print(f"{list[comp-1]} Computer Won Because it Choose {game_names[comp-1]}.")
elif(comp==3 and players_choice==1):
    print(f"{list[comp-1]} Congratulation You Won Computer Choose {game_names[comp-1]}.")
elif comp==players_choice:
    print(f"{list[comp-1]} Game Drawn Because Both Choose: {game_names[comp-1]}")
else:
    print("You Loose Because you choose the Incorrect Option.")