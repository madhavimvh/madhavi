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
