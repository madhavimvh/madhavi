'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    str_input = input()
    a_n = ""
    for c_h in str_input:
        if c_h in ('!', '@', '#', '$', '%', '^', '&', '*'):
            a_n += " "
        else:
            a_n += c_h
    print(a_n)

if __name__ == "__main__":
    main()
