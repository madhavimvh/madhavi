'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    S = str(input())
    Z = ""
    for nn in S:
        if nn == "!" or nn == "@" or nn == "#" or nn == "$" or nn == "%" or nn == "^" or nn == "&" or nn == "*":
             Z += " "
        else:
            Z += nn
    print(Z)        
main()
