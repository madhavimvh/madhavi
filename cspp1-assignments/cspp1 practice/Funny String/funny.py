def funnyornot(s):
	rs = s[::-1]
	n = len(s)
	for i in range(1, n):
		d1 = abs(ord(s[i]) - ord(s[i - 1]))
		d2 = abs(ord(rs[i]) - ord(rs[i - 1]))
		if d1 != d2:
			return "Not Funny"
			break
	else:
		return "Funny"







def main():
	cases = int(input())
	a = []
	for caseNo in range(cases):
	    s = input()
	    a.append(s)
	    # print(a)
	for i in range(len(a)):
		print(funnyornot(a[i]))
	    
if __name__ == "__main__":
    main()	        