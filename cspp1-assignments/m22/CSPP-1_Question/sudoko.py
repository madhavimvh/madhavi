def print_grid(arr): 
    for i in range(9): 
        print(arr[i]) 
def create_set(g, row, col):
    lis= set()
    for i in range(9):
        if g[row][i] != '0':
            lis.add(g[row][i])
        if g[i][col] != '0':
            lis.add(g[i][col])
    return lis

def possibilities(g):
    for i in range(9):
        for j in range(9):
            res = ""
            s = set()
            if g[i][j] == '0':
                s = create_set(g, i, j)
                # print(s)
            if len(s) != 0:
                for each in "123456789":
                    if each not in s:
                        res += each
                print(res)

if __name__=="__main__": 
      
    # creating a 2D array for the grid 
    grid=[['0' for x in range(9)]for y in range(9)] 
    print_grid(grid)
      
    given_input = input()
    k = 0
    for i in range(9):
        for j in range(9):
            if given_input[k] != '.':
                grid[i][j] = given_input[k]
            k += 1
    print_grid(grid)
    possibilities(grid)




# def main():
#     string = input()
#     string = list(string)
#     grid = []
#     grid1 = []
#     for i in range(81):
#         if i%9 == 0 and i != 0:
#             grid.append(grid1)
#             grid1 = []
#         grid1.append(string[i])
#     grid.append(grid1)
#     # print(grid)
#     for i in range(9):
#         for j in range(9):
#             if grid[i][j] == ".":
#                 print(sudoku(grid, i, j))
# def sudoku(grid, i, j):
#     grid2 = []
#     for row in range(9):
#         grid2.append(grid[row][j])
#     for col in range(9):
#         grid2.append(grid[i][col])
#     # print(grid2)
#     if (i >= 0 and i <= 2) and (j >= 0 and j < 3):
#         for subrow in range(0, 3):
#             for subcol in range(0, 3):
#                 grid2.append(grid[subrow][subcol])
#     if (i >= 0 and i < 3) and (j >= 3 and j < 6):
#         for subrow in range(0, 3):
#             for subcol in range(3, 6):
#                 grid2.append(grid[subrow][subcol])
#     if (i >= 0 and i < 3) and (j >= 6 and j < 9):
#         for subrow in range(0, 3):
#             for subcol in range(6, 9):
#                 grid2.append(grid[subrow][subcol])
#     if (i >= 3 and i < 6) and (j >= 0 and j < 3):
#         for subrow in range(3, 6):
#             for subcol in range(0, 3):
#                 grid2.append(grid[subrow][subcol])
#     if (i >= 3 and i < 6) and (j >= 3 and j < 6):
#         for subrow in range(3, 6):
#             for subcol in range(3, 6):
#                 grid2.append(grid[subrow][subcol])
#     if (i >= 3 and i < 6) and (j >= 6 and j < 9):
#         for subrow in range(3, 6):
#             for subcol in range(6, 9):
#                 grid2.append(grid[subrow][subcol])
#     if (i >= 6 and i < 9) and (j >= 0 and j < 3):
#         for subrow in range(6, 9):
#             for subcol in range(0, 3):
#                 grid2.append(grid[subrow][subcol])
#     if (i >= 6 and i < 9) and (j >= 3 and j < 6):
#         for subrow in range(6, 9):
#             for subcol in range(3, 6):
#                 grid2.append(grid[subrow][subcol])
#     if (i >= 6 and i < 9) and (j >= 6 and j < 9):
#         for subrow in range(6,9):
#             for subcol in range(6,9):
#                 grid2.append(grid[subrow][subcol])
#     # print(grid2)
#     string = ''.join(grid2)
#     string = string.replace(".", "")
#     string = list(string)
#     inti = list(map(int,string))
#     whole = [1,2,3,4,5,6,7,8,9]
#     numbers = []
#     for h in range(len(whole)):
#         if whole[h] not in inti:
#             numbers.append(whole[h])
#     string1 = list(map(str,numbers))
#     string1 = ''.join(string1)
#     return string1

#     # print(gridlist)


    
# main()