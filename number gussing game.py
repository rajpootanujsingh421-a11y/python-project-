import random
secret = random.randint(1,10)

while True:
    guess = int(input("Enter your guess"))

    if guess == secret:
        print("Congratulations!")
        break
    elif guess > secret:
        print("Too high!")
    else:
        print("Too low!")
    