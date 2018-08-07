"""
# Exercise: Assignment-2
# Write a Python function, sumofdigits, that takes in one number and
 returns the sum of digits of given number.
# This function takes in one number and returns one number.
"""
def sumofdigits(var_n):
    '''
    n is positive Integer
    returns: a positive integer, the sum of digits of n.
    '''
    while var_n >= 0:
        if var_n == 0:
            return 0
        return (var_n % 10) + sumofdigits(var_n//10)
def main():
    """It is a main function"""
    var_a = input()
    print(sumofdigits(int(var_a)))
if __name__ == "__main__":
    main()
