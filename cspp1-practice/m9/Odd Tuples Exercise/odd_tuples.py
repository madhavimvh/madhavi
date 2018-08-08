#Exercise : Odd Tuples
#Write a python function oddTuples(aTup) that takes a some numbers in the tuple as input and returns a tuple in which contains odd index values in the input tuple  



def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    i= 0
    b = len(aTup)
    c =()
    while (i < b):
        if i%2 != 0:
            i += 1
        else:
            c += (aTup[i],)
            i += 1
    return(c)
            
        

def main():
    data = input()
    data = data.split(" ")
    aTup=()
    for j in range(len(data)):
        aTup += (int(data[j]),)
    print(oddTuples(aTup))
        

if __name__ == "__main__":
    main()
