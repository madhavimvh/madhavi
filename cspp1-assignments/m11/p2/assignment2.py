"""program to update hand"""
#Exercise: Assignment-2
#Implement the updateHand function. Make sure this function has no side effects: i.e., it must not mutate the hand passed in. Before pasting your function definition here, be sure you've passed the appropriate tests in test_ps4a.py.


def update_Hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    
    for letter in word:
        if letter in hand:
            hand[letter]=hand[letter] - 1
    return hand
            
        
    
"""
n_n is the int input, adict is hand and data1 is the word"""
def main():
	n_n=input()
	adict={}
	for i in range(int(n_n)):
		data=input()
		l_l=data.split()
		adict[l[0]]=int(l_l[1])
	data1=input()
	print(update_Hand(adict,data1))
		


if __name__== "__main__":
	main()
