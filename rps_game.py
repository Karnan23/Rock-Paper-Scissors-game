#rock,paper,scissor gamer
import random

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'

emojis = {
    ROCK: '✊',
    PAPER: '✋',
    SCISSORS: '✌️'
}
choices=tuple(emojis.keys())

def get_user_choice():
    while True:
        user_choice = input("Rock,paper or scissor(r,p,s): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("invalid choice!")

def display_choices(user_choice, computer_choice):
    print(f"Your choice: {emojis[user_choice]}")
    print(f"Computer choice: {emojis[computer_choice]}")

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print( "It's a tie!")
        return 0
    elif ((user_choice == ROCK and computer_choice == SCISSORS) or
          (user_choice == PAPER and computer_choice == ROCK) or
          (user_choice == SCISSORS and computer_choice == PAPER)):
       print("You win!")
       return 1
    else:
        print( "You lose!")
        return -1

def overall_winner(user_count, computer_count):
    if user_count > computer_count:
        print("You are the overall winner!")
    elif user_count < computer_count:
        print("Computer is the overall winner!")
    else:
        print("It's a tie overall!")
    print("Thanks for playing!")

def want_continue(user_count, computer_count):
    should_continue = input("Do you want to play again? (y/n): ").lower()
    if should_continue !='n':
        while should_continue not in ['y']:
            print("Invalid input! Please enter 'y' or 'n'.")
            should_continue = input("Do you want to play again? (y/n): ").lower()
            continue
    elif should_continue=='n':
         overall_winner(user_count, computer_count)



def play_game():
    user_count=0
    computer_count=0
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(choices)
        display_choices(user_choice, computer_choice)
        result=winner(user_choice, computer_choice)
        if result == 1:
            user_count += 1
        elif result == -1:
            computer_count += 1
            
        should_continue = input("Do you want to play again? (y/n): ").lower()
        if should_continue == 'n':
            overall_winner(user_count, computer_count)
            break  # exit the play_game function
        elif should_continue == 'y':
            continue
        else:
            print("Invalid input! Please enter 'y' or 'n'.")
            want_continue(user_count, computer_count)
            
        

play_game()
# This is a simple rock-paper-scissors game where the user plays against the computer.
