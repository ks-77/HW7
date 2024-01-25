"""
HW7
Savchenko Kirill
"""
import random
import sys


# 1


def get_number_pow(number, number_pow):
    if number_pow <= 1:
        return number

    return number * get_number_pow(number, number_pow - 1)


number_inp = int(input("Enter a number: "))
number_exp_inp = int(input("Enter a number exponent: "))
result = get_number_pow(number_inp, number_exp_inp)
print(f"\nyour number: '{number_inp}' raised to the power: '{number_exp_inp}' = {result}")

# 2


def stars(number_of_stars):
    if number_of_stars == 0:
        return ""

    print("*", end=" "), stars(number_of_stars - 1)
    return ""


print(stars(int(input("Enter a number of stars: "))))
# IDK how to explain this by writing smth similar as in the lesson,but if in general:
# if input number != 0 then the * is printed,end=" "- gives us ability to add str,(* )not column,in the next recursion
# and start working function and the main recursive function calls itself, but with the parameter dynamically decreased
# by 1 each time it is called and when the parameter value reaches 0 the function completes its action and returns ""

# 3


def span(a, b):
    if a <= b:
        if a == b:
            return a
        return a + span(a + 1, b)
    elif a >= b:
        return b + span(a, b + 1)


a_inp = int(input("Enter first number: "))
b_inp = int(input("Enter second number: "))
print(f"sum of numbers between '{a_inp}' and '{b_inp}' (inclusive) = {span(a_inp, b_inp)}")

# a = 1, b = 5
# span(1, 5) -> 1 + span(2, 5) => 3
# span(2, 5) -> 1 + span(3, 5) => 6
# span(3, 5) -> 1 + span(4, 5) => 10
# span(4, 5) -> 1 + span(5, 5) => 15
# span(5, 5) => 1
# writing functions is much easier than explaining them, hope wrote it true

# 4


def min_num_spam(len_span, start_index=0, min_sum=sys.maxsize, min_sum_index=None):
    if start_index + 10 > len(len_span):
        return min_sum_index
    sum_actual = min(len_span[start_index: start_index + 10])

    if min_sum > sum_actual:
        min_sum = sum_actual
        min_sum_index = start_index

    return min_num_spam(len_span, start_index + 1, min_sum, min_sum_index)


total_span = [random.randint(0, 100) for _ in range(100)]
print(f"Total span: {total_span}")
print(f"index from which the ten numbers with the minimum sum begin: {min_num_spam(total_span)}")
