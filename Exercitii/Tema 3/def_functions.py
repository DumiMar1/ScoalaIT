def palidrom(num):

    if str(num) == str(num[::-1]):
        return True
    else:
        return False


def is_prime(num):

    num = int(num)
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


def divisor(num):

    divisors_list = []
    num = int(num)
    for i in range(2, num):
        if num % i == 0:
            divisors_list.append(i)
    return divisors_list


def max_divisor(num):

    return max(divisor(num))


def digits(num):
    return len(num)

