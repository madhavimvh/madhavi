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
    def main():
    s = str(input())
    z = ""
    for n in s:
        if n =="!" or n =="@" or n =="#" or n =="$" or n =="%" or n =="^" or n =="&" or n =="*":
             z+=" "
        else:
            z+=n
    print(z)        
main()
