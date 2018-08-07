"""
program to determine the base to the power
"""
# Exercise: PowerRecr
# Write a Python function, recurPower(base, exp),
#that takes in two numbers and returns the base^(exp) of given base and exp.
# This function takes in two numbers and returns one number.


def recur_power(ba_se, exp):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    if exp == 1:
        return ba_se
    return ba_se*recur_power(ba_se, exp-1)
def main():
    """
    main function that calls itself
    """
    data = input()
    data = data.split()
    print(recur_power(float(data[0]), int(data[1])))
main()
