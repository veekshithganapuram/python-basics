import random

number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("Guess a number between 1 and 100: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    attempts += 1

    if guess < 1 or guess > 100:
        print("Out of range. Try again.")
    elif guess < number:
        print("Too low.")
    elif guess > number:
        print("Too high.")
    else:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break
