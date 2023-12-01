import random


def number_guesser():
    # Set the target number
    target_number = random.randint(1, 50)

    # Set the number of guesses remaining
    chances_left = 5

    print("Welcome to the Number Guesser App!")
    print("Guess a number between 1 and 50.")

    while chances_left > 0:
        # Get user input
        guess = int(input("Enter your guess: "))

        if guess == target_number:
            print("Congratulations! You guessed the correct number.")
            break
        elif guess < target_number:
            print("Hint: The correct number is greater.")
        else:
            print("Hint: The correct number is smaller.")

        chances_left -= 1
        print(f"Chances left: {chances_left}")

    if chances_left == 0:
        print(f"Ups!!! you left no  chances. The correct number was {target_number}.")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    return play_again == 'yes'


def main():
    while True:
        if not number_guesser():
            break


if __name__ == "__main__":
    main()
