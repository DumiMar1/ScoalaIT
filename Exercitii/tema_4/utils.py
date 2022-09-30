import random
words_list = ["Canada", "Argentina", "China", "Germania", "Australia", "Romania", "Liechtenstein", "Monaco", "Vatican", "Mexic"]
player_lives = 3

computer_choice = random.choice(words_list).lower()
computer_choice_hidden = "_" * len(computer_choice)


def user_guess_f():
    while True:
        user_guess = input("Please provide a char.")
        if user_guess.isalpha():
            return user_guess.lower()


def index_list_f(user_guess, string):
    index_list_1 = []
    for index1 in range(len(string)):
        if string[index1] == user_guess:
            index_list_1.append(index1)
    return index_list_1


def replace_char(char, string, lst):
    list_string = list(string)
    for index in lst:
        list_string[index] = char
    return str("".join(list_string))



