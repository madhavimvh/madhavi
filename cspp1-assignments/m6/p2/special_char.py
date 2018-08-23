'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    s = input()
    a = "!@#$%^&*"
    #a_list = list(a)
    s_new = ""
    for letter in s:
        if letter not in a:
            print(letter)
            s_new += letter
        else:
            s_new += " "
            
    print(s_new)
main()
    
































"""
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    s = str(input())
    z = ""
    for n in s:
        if n == "!" or n == "@" or n == "#" or n == "$" or n == "%" or n == "^" or n == "&" or n == "*":
             z+=" "
        else:
            z+=n
    print(z)     
main()
"""
