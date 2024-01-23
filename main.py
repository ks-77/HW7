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
