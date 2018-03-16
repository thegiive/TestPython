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

input_list = [3,1,2,5,4,6]
print(find_second_largest_element(input_list))
