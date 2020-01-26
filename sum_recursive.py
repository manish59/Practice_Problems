def Sum(arr):
    result=0
    #print(arr)
    if len(arr)==1:
        return arr[0]
    elif len(arr)==0:
        return 0
    else:
        return arr[len(arr)-1]+Sum(arr[:len(arr)-1])
print(Sum([1,2,3,4])) 