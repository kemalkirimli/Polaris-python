import random

secret_number = random.randint(1, 100)
guessCount = 0

print("The number between 1 and 100. Try to guess it!")

while True:
    try:
        guess = int(input("Your guess: "))
        guessCount += 1

        if guess < 1 or guess > 100:
            print(" Enter a number between 1 and 100.")
        elif guess < secret_number:
            print("Go higher")
        elif guess > secret_number:
            print("Go lower")
        else:
            print(f"Congratulations :) You guessed it in {guessCount} tries!")
            break

    except ValueError:
        print("Please enter a valid number!")
