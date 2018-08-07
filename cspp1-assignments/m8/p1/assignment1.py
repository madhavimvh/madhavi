"""
# Exercise: Assignment-1
# Write a Python function, factorial(n).
# This function takes in one number and returns one number.
"""
def factorial(var_n):
    '''
    n is positive Integer
    returns: a positive integer, the factorial of n.
    '''
    if var_n == 0:
        return 1
    return var_n * factorial(var_n - 1)
def main():
    """It is a main function"""
    var_a = input()
    print(factorial(int(var_a)))
if __name__ == "__main__":
    main()
