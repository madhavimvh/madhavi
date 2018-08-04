def main():
    n = int(input())
    p=1
    i=1
    while n>0:
        rem = n%10
        p = p*rem
        n = n//10
    print(p)
main()
        
        
