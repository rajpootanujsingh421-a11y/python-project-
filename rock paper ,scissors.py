import random
choices = ["rock","paper","scissors"]
user = input("Choose rock,paper or scissors:").lower()
computer = random.choice(choices)
print("you:",user)
print("Computer:",computer)
if user == computer:
    print("Draw!")
elif (user == "rock" and computer == "scissors"):
    print("you Win!")
elif (user == "scissors" and computer == "paper"):
    print("You Win!")
elif (user == "paper" and computer == "rock"):
    print("You Win!")
else:
    print("Computer Win!")
