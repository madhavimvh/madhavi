def main():
    s = str(input("enter a string"))
    b=len(s)
    i=1
    while i<=b:
        for n in s:
            if n =="!" or n =="@" or n =="$" or n =="%" or n =="^" or n =="&" or n =="*":
                str(n) = " " 
                i=i+1
                print(s)
main()
