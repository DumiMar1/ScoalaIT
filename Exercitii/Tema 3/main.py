from def_functions import *


def user_input_f():

    control_list = ["quit", "exit"]

    while True:
        user_input = input("Please provide an integer. Or quit/exit to finish.")

        if user_input.isdigit():
            return {"is_palindrome": palidrom(user_input),
                    "is_prime": is_prime(user_input),
                    "divisors": divisor(user_input),
                    "max_divisor": max_divisor(user_input),
                    "digits": digits(user_input)
                    }

        elif user_input.lower() in control_list:
            print("You finished the program.")
            break


print(user_input_f())
