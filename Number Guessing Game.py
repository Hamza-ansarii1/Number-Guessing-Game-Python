import random

# Randon number generate between 1 and 10
secret_number = random.randint(1,10)


while True:

    guess = int(input("Guess the number (1-10): "))

    if guess == secret_number:
        print("correct! you gueesed it.")
        break

    elif guess > secret_number:
        print("Too high! Try again")

    else:
        print("Too Low! Try again")
       