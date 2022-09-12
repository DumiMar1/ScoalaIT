#
#
# def say_something(user_input):
#     empty_list = []
#
#     while True:
#
#         if user_input.startswith(("How", "What", "Where", "When")):
#             empty_list.append(user_input + "? ")
#
#         if user_input:
#             empty_list.append(user_input.capitalize() + ". ")
#
#         return "".join(empty_list)
#
#
# user_input = input("say something: ")
# print(say_something(user_input))
#
#

def str_input(string):

    for index in range(len(string)):

        if string[index] == "(" and string[index + 1] == ")":
            return True
        else:
            return False

print(str_input("()"))
