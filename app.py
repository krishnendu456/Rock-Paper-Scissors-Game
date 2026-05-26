import random

choices = ["rock", "paper", "scissors"]

print("=== Rock Paper Scissors Game ===")

while True:

    user = input("\nEnter rock, paper, or scissors: ").lower()

    if user not in choices:
        print("Invalid choice!")
        continue

    computer = random.choice(choices)

    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")

    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("You win!")

    else:
        print("Computer wins!")

    again = input("\nPlay again? (yes/no): ").lower()

    if again != "yes":
        print("Thanks for playing!")
        break