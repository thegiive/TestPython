def makeArrayConsecutive2(statues):
    result = 0 
    sorted_statues = sorted(statues)
    for i in range(0,len(sorted_statues)-1):
        result += sorted_statues[i+1] - sorted_statues[i] -1 
    return result

array_list = [6, 2, 3, 8]
print(makeArrayConsecutive2(array_list))