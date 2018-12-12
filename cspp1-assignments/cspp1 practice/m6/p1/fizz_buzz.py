'''
Write a short program that prints each number from 1 to num on a new line.
For each multiple of 3, print "Fizz" instead of the number.
For each multiple of 5, print "Buzz" instead of the number.
For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
'''
def main():
    '''
    Read number from the input, store it in variable num.
    '''
    num = int(input())
    for i in range(num):
	    if num % 3 and num % 5 == 0:
	    	print("FizzBuzz")
	    if num % 3 == 0:
	    	print("Fizz")
	    if num % 5 == 0:
	    	print("Buzz")
	    else:
	    	print(i)

if __name__ == "__main__":
    main()
