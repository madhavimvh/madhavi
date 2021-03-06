# Exercise: Assignment-2
# Write a Python function, sumofdigits, that takes in one number and returns the sum of digits of given number.

# This function takes in one number and returns one number.


def sumofdigits(n):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    # Your code here
    summ = 0
    rem = 0
    while n > 0:
    	rem = n % 10
    	summ = summ + rem
    	n = n//10
    return summ


def main():
    a = input()
    print(sumofdigits(int(a)))  

if __name__== "__main__":
    main()

