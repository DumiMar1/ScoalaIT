def user_input_f():

    control_list = ["quit", "exit", "0"]

    while True:
        user_input = input("Please provide an integer(not 0). Or quit/exit to finish.")

        if user_input.lower() in control_list:
            user_input = None
            print("You finished the program! ")
            break

        try:
            user_input == int(user_input)

        except ValueError:

            user_input = None

        if user_input is not None:
            break
    return user_input


def is_palindrome(num):

    return str(num) == str(num[::-1])


def divisor(num):

    divisors_list = []
    num = abs(int(num))
    for i in range(2, num):
        if num % i == 0:
            divisors_list.append(i)
    return divisors_list


def digits(num):
    count = 0
    num = abs(int(num))
    while num != 0:
        num //= 10
        count += 1
    return count


def get_output(num):
    div = divisor(num)
    div_len = len(div)
    num_data = {"is_palindrome": is_palindrome(num),
                "is_prime": div_len == 0,
                "divisors": div,
                "max_divisor": max(div) if div_len > 0 else None,
                "digits": digits(int(num))
                }
    return num_data

