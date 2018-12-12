'''
Given a  number int_input, find the product of all the digits
example: 
	input: 123
	output: 6
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    n = int(input())
    product = 1
    if n == 0:
    	print(n)
    elif n > 0:
    	while n > 0:
    		rem = n % 10
    		product = product*rem
    		n = n//10
    	print(product)
    else:
    	n = -n
    	while n > 0:
    		rem = n % 10
    		product = product*rem
    		n = n//10
    	print(-product)

if __name__ == "__main__":
    main()
