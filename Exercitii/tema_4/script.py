from utils import *

if __name__ == "__main__":
    print("This game contains names of countries.")
    print(f"Your word to guess is {computer_choice_hidden}.")

    while computer_choice.lower() != computer_choice_hidden and player_lives != 0:
        valid_input = user_input()
        index_list = index_lst(valid_input, computer_choice)
        replaced_string = replace_char(valid_input, computer_choice_hidden, index_list)

        if valid_input in computer_choice.lower():
            computer_choice_hidden = replaced_string
            print(f"Your word to guess is {replaced_string}.")
            if computer_choice_hidden == computer_choice.lower():
                print(f"You won! The word was '{computer_choice}'")

        else:
            player_lives -= 1
            print(f"You have {player_lives} lives left.")

    if player_lives == 0:
        print("You lost .")























