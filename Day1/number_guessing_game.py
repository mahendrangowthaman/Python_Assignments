import random

number = random.randint(1, 100)
guess = int(input("Enter your guess (1 to 100): "))

while guess != number:
    if guess < 1 or guess > 100:
        print("Invalid input! Please enter a number between 1 and 100.")
    elif guess < number:
        print("The guessed number is LESSER than the actual number.")
    else:
        print("The guessed number is GREATER than the actual number.")
    
    guess = int(input("Enter your guess again (1 to 100): "))

print("Correct! You guessed the number.")
