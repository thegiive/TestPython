# https://codefights.com/arcade/intro/level-2/xzKiBHjhoinnpdh6m
def find_second_largest_element(element_list):
    max = float('-inf')
    second_max = float('-inf')
    for ele in element_list:
        if(ele > max):
            second_max = max
            max = ele
        elif(ele > second_max):
            second_max = ele
    return second_max



# def adjacentElementsProduct(inputArray):
#     max1 = max(inputArray)
#     inputArray.remove(max1)
#     max2 = max(inputArray)
#     inputArray.append(max1)
#     min1 = min(inputArray)
#     inputArray.remove(min1)
#     min2 = min(inputArray)
#     print(max1)
#     print(max2)
#     print(min1)
#     print(min2)
#     if(max1 * max2 > min1 *min2):
#         return max1*max2 
#     else:
#         return min1*min2


def adjacentElementsProduct(inputArray):
    max = float('-inf')
    for i in range(0,(len(inputArray)-1) ):
        if( inputArray[i] * inputArray[i+1] > max):
            max = inputArray[i] * inputArray[i+1]
    return max

# input_list = [3,1,2,5,4,6 , -10 , -20 ]
input_list = [3, 6, -2, -5, 7, 3]
print(adjacentElementsProduct(input_list))
# print(find_second_largest_element(input_list))
# print(adjacentElementsProduct(input_list))
