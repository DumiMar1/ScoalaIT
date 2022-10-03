import random
words_list = ["Canada", "Argentina", "China", "Germania", "Australia", "Romania", "Liechtenstein", "Monaco", "Vatican", "Mexic"]
player_lives = 3

computer_choice = random.choice(words_list)
computer_choice_hidden = "_" * len(computer_choice)


def user_input():
    while True:
        user_guess = input("Please provide a char.")
        if user_guess.isalpha() and len(user_guess) == 1:
            return user_guess


def index_lst(user_guess, string):
    index_list = []
    for index in range(len(string)):
        if string[index].lower() == user_guess:
            index_list.append(index)
    return index_list


def replace_char(char, string, lst):
    list_string = list(string)
    for index in lst:
        list_string[index] = char
    return str("".join(list_string))



