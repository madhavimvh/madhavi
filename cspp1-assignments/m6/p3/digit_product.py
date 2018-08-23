'''
Given a  number int_input, find the product of all the digits
example: 
	input: 123
	output: 6
'''
def main():
    s = int(input())
    sum = 1
    while s > 0:
        print(s)
        rem = s%10
        sum = sum*rem
        s = s//10
    print(sum)
main()
    































"""
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    s = str(input())
    z = ""
    for n in s:
        if n =="!" or n =="@" or n =="#" or n =="$" or n =="%" or n =="^" or n =="&" or n =="*":
             z+=" "
        else:
            z+=n
    print(z)        
main()"""
