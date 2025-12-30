import random

choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0

while True:
    user = input("Enter rock, paper, or scissors (or quit to stop): ").lower()

    if user == "quit":
        break

    if user not in choices:
        print("Invalid choice. Try again.")
        continue

    computer = random.choice(choices)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    print("Score → You:", user_score, "| Computer:", computer_score)
    print("-" * 30)

print("\nFinal Score")
print("You:", user_score)
print("Computer:", computer_score)
print("Thanks for playing!")
