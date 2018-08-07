"""
program to find the base to the power
"""
# Exercise: PowerIter
# Write a Python function, iterPower(base, exp),
# that takes in two numbers and returns the base^(exp) of given base and exp.
# This function takes in two numbers and returns one number.


def iter_power(ba_se, ex_p):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^ex
    p
    '''
    if ex_p == 1:
        return ba_se
    m_m = ba_se
    while ex_p >= 0:
        m_m = ba_se*m_m
        ex_p = ex_p - 2
    return m_m
    #Your code here
def main():
    """
    main function that calls itself
    """
    data = input()
    data = data.split()
    print(iter_power(float(data[0]), int(data[1])))
main()
