def matrixElementsSum(matrix):
    for index_1 in range(1,len(matrix)):
        for index_2 in range(0,len(matrix[index_1])):
            if(matrix[index_1-1][index_2] ==0):
                matrix[index_1][index_2] = 0 
    result = 0 
    for arr in matrix:
        for ele in arr:
            result+= ele 
    return result 
        

print(matrixElementsSum([[1,1,1,0], [0,5,0,1], [2,1,3,10]]))
# [[1,1,1,0], 
#  [0,5,0,1], 
#  [2,1,3,10]]