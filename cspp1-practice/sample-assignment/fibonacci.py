def main():
    n = int(input())
    x = 0
    print(x)
    y = 1
    print(y)
    for i in range(1, n):
        z = x + y
        x = y
        y = z
        print(z)
main()
        
