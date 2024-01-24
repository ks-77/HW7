"""
HW7
Savchenko Kirill
"""

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