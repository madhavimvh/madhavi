def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        print("len",len(L)//2)
        left = merge_sort(L[:middle])
        print("1l",left)
        right = merge_sort(L[middle:])
        #return merge(left, right)
        print("l",left)
        print("r",right)
    return L
"""def merge(left, right):
    result = []
    if left < right:
        result = left + right
    return result"""
    
    
print(merge_sort([2,3,7,9,5,4,8,6]))
