def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    size_m1 = len(m1)
    size_n1 = len(m1[0])
    size_m2 = len(m2)
    size_n2 = len(m2[0])
    result = [0]*size_m1
    for each in range(len(result)):
        result[each] = [0]*size_n2
    #print(result)
    
        
    
    if size_n1 == size_m2:
        for i in range(size_m1):
            #print(i)
            for j in range(size_n2):
                #print(j)
                for k in range(size_m2):
                    #print(k)
                    result[i][j] += int(m1[i][k]) * int(m2[k][j])
        return result
    else:
        print("Error: Matrix shapes invalid for mult")
    

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    result = []
    if len(m1) == len(m2):
        for i in range(len(m1)):
            #print(i)
            if len(m1[i]) == len(m2[i]):
                for j in range(len(m1[0])):
                    if j == 0:
                        result1 = []
                        result.append(result1)
                    #print(j)
                    result1.append(int(m1[i][j]) + int(m2[i][j]))
                    #print(m1[i][j])
                    #print(m2[i][j])
                    #print(result)
        #print(result)
        return result
    else:
        print("Error: Matrix shapes invalid for addition")
        
def read_matrix(n):
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    rows = int(n[0])
        #print("n",n[0])
    cols = int(n[2])
    """for i in range(rows):
            mat = []
            print(mat)"""
        
    mat = []
    for i in range(rows):
    #print("i",i)
        mat.append(input().split(" "))
        #print("s",mat)
    #print("spk",mat)
    #return mat
    flag = 0
    for j in range(len(mat)):
        if len(mat[j]) == cols:
            #print(mat[j])
            #print(len(mat[j]))
            #print(cols)
            flag = 1
        else:
            print("Error: Invalid input for the matrix")
            return False
    return mat

            

def main():
    n = input()
    # read matrix 1
    global m1
    m1 = read_matrix(n)
    #print("m1",m1)
    
    # read matrix 2
    m = input()
    global m2
    m2 = read_matrix(m)
    #print("m2",m2)
    if m1 != False and m2 != False:
        # add matrix 1 and matrix 2
        print(add_matrix(m1, m2))
        #return add_matrix(m1, m2)

        # multiply matrix 1 and matrix 2
        print(mult_matrix(m1, m2))
        #return mult_matrix(m1, m2)
        

if __name__ == '__main__':
    main()
