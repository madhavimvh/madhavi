#Exercise : how many
# write a procedure, called how_many, which returns the sum of the number of values associated with a dictionary.


def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    c = 0
    for i in aDict:
        b = len(aDict[i])
        c += b
    return(c)
    

def main():
    n=input()
    aDict={}
    for i in range(int(n)):
        s=input()
        l=s.split()
        if l[0] not in aDict:
            aDict[l[0]]=[l[1]]
        else:
            aDict[l[0]].append(l[1])
    # print(aDict)
    print(how_many(aDict))

if __name__== "__main__":
    main()
