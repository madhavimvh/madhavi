def main():
    n = int(input())
    p=1
    i=1
    if n==0:
        print("0")
    if n!=0:
        while n>0:
            rem = n%10
            p = p*rem
            n = n//10
    print(p)
main()
        
        
