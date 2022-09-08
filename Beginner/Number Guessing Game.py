import random
from typing import List, Any

attempts_list = []


def show_score():
    if len(attempts_list) <= 0:
        print("****There is currently no high score in this game. Play game to earn a high score****")
    else:
        print("The current high score is: ", max(attempts_list))


def start_game():
    print("Welcome to the number guessing game!!!")
    show_score()
    random_number = int(random.randint(1, 10))
    player_name = input("What is your name?: ")

    consent = input("Hi " + player_name + ", would you like to play this game? (Enter y/n) ")
    attempts = 0
    while consent.lower() == "y":
        try:
            guess = int(input("Pick a number between from 1 to 10: "))
            if guess < 1 or guess > 10:
                raise ValueError("Please enter a number between 1 and 10")
            if guess == random_number:
                print("Congratulations! You guessed right!")
                attempts = + 1
                attempts_list.append(attempts)
                print("It took you ", attempts, "attempt(s) to guess right")

                play_again = input("Would you like to play again? (Enter y/n): ")
                attempts = 0

                show_score()

                random_number = int(random.randint(1, 10))

                if play_again.lower() == "n":
                    print("Okay! Sad to see you go")
                    print("Game ended")
                break
            elif guess > random_number:
                print("Your guess is higher")
                attempts = + 1
            elif guess < random_number:
                print("Your guess is lesser")
                attempts = + 1
        except ValueError:
            print("Sorry!, that is not a valid value.Try again!")
    else:
        print("That's fine, sad to see you go!")


if __name__ == '__main__':
    start_game()
