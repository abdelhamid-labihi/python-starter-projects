import random

attempts_list = []

def show_score():
    if not attempts_list:
        print("There's currently no high score, start playing!")
    else:
        print(f"The current high score is {min(attempts_list)} attempts")

while True:
    print("Hello player! Welcome to the guessing game!")
    player_name = input("What's your name? ")
    
    lower_bound = int(input(f"Hi, {player_name}, please enter the lower bound of the range: "))
    upper_bound = int(input("Now, please enter the upper bound of the range: "))
    
    print(f"Great! Now, please guess a number between {lower_bound} and {upper_bound}.")
    player_choice = int(input())
    pc_choice = random.randint(lower_bound, upper_bound)
    attempts = 1

    while player_choice != pc_choice:
        if player_choice < pc_choice:
            print("Too low, try again.")
        else:
            print("Too high, try again.")
        player_choice = int(input())
        attempts += 1

    attempts_list.append(attempts)
    show_score()

    print("Congratulations! You have guessed the number in", attempts, "attempts.")
    play_again = input("Do you want to play again? (yes/no)")
    if play_again.lower() == "no":
        print("That's cool, have a good day.")
        break