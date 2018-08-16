DICTIONARY = {'T' : "10", 'J' : "11", 'Q' : "12", 'K' : "13", "A" : "14"}
def is_fourofakind(hand):
    global hands_four
    hands_four = []
    for n_n in range(len(hand)):
        if hand[n_n][0] in DICTIONARY:
            hands_four.append(DICTIONARY[hand[n_n][0]])
        else:
            hands_four.append(hand[n_n][0])
    #print(hands_four)
    global s
    s = set(hands_four)
    #print(s)
    if len(s) == 2:
        for k in range(len(hands_four)):
            c = hands_four.count(hands_four[k])
            if c == 4:
                return True
            return False

def is_threeofakind(hand):
        is_fourofakind(hand)
        if len(s) == 3:
            for i in range(len(hands_four)):
                c = hands_four.count(hands_four[i])
                #print(c)
                if c == 3 and c !=2:
                    return True
        return False
def is_twopair(hand):
    res = ""
    j = 0
    res = 0
    is_fourofakind(hand)
    for i in range(len(hands_four)):
        c = hands_four.count(hands_four[i])
        #print(c)
        if c == 2 and c != 3:
            j += 1
            #print("j",j)
            if j == 4:
                return True
    return False
def is_fullhouse(hand):
    is_fourofakind(hand)
    j = 0
    if len(s) == 2:
        for i in range(len(hands_four)):
            c = hands_four.count(hands_four[i])
            #print(c)
            if c != 4:
                if c == 3 or c == 2:
                    j += 1
                    #print(j)
                    if j == 5:
                        return True
        return False
            
            
def is_onepair(hand):
    is_fourofakind(hand)
    if len(s) == 4:
        return True
    return False


print(is_fourofakind(['4C', '4S', '4D', '4S', '5D']))
#print(is_threeofakind(['5C', '4S', '4D', '7S', '7D']))
#print(is_onepair(['5C', '4S', '4D', '3S', '7D']))
#print(is_twopair(['5C', '4S', '4D', '7S', '7D']))
print(is_fullhouse(['4C', '4S', '4D', '4S', '5D']))
