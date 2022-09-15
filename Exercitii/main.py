#Temă Data Structures
my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
my_list.sort()
print(my_list)
print(my_list[::-1])
print(my_list[1::2])
print(my_list[0::2])
print(my_list[2::3])

#Temă Functions

#1.Să se scrie o funcție care primește un număr nedefinit de parametrii și să se calculeze
#            suma parametrilor care reprezintă numere întregi sau reale.



def your_function(*args, **kwargs):
    empty_list = []

    for item in args:
        if type(item) == int:
            empty_list.append(item)

    return sum(empty_list)


print(your_function(1, 5, -3, "abc" , [12, 56, "cad"]))

print(your_function())

print(your_function(2, 4, "bc", param_1=2))


#2.Să se scrie o funcție recursivă care primește ca parametru un număr întreg și returnează:

def sum_nums(num):
    count_even = 0
    count_odd = 0
    count = 0
    for item in range(num + 1):
        count += item
        if item % 2 == 0:
            count_even += item
        if item % 2 != 0:
            count_odd += item
    return f"sum of all numbers: {count}, sum of odd numbers: {count_odd} and sum of even numbers: {count_even}"


print(sum_nums(10))


#3. Să se scrie o funcție care citește de la tastatură și returnează valoarea dacă aceasta este un număr întreg,
# altfel returnează valoarea 0.

def read_return_func():
    user_input = input("Please provide a number: ")

    try:
        user_int = int(user_input)

    except ValueError:
        print(0)

    else:
        return user_input


print(read_return_func())
