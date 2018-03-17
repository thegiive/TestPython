def shapeAreaNoneRec(n):
    # 1 5 13 25    => 4 8 12 
    if(n == 1):
        return 1 
    else:
        return shapeArea(n-1) + 4 * ( n-1)

def shapeArea(n):
    result = 1 
    for i in range(1,n+1):
        result += 4 * ( i - 1)
    return result

print(shapeArea(1000))