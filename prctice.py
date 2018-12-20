
def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result
def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1
def main():
	print(applyEachTo([inc, max, int], -3))
if __name__ == "__main__":
    main()