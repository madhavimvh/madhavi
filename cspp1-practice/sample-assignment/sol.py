"""
def main():
	n = input()
	dict = {}
	for i in range(int(n)):
		val = input()
		val_list = val.split(" ")
		print(val_list)
		if val_list[0] not in dict:
			dict[val_list[0]] = [val_list[1]]
		elif val_list[1] not in dict[val_list[0]] :
			dict[val_list[0]].append(val_list[1])
	print(dict)
if __name__== "__main__":
	main()"""
def calculateHandlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """
    sum = 0
    for letter in hand:
        sum = sum + hand[letter]
    return sum




