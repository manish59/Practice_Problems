def bs(array,key):
    low=0
    high=len(array)-1
    while(low<=high):
        mid=(low+high)/2
        mid=int(mid)
        #print(mid)
        guess=array[mid]
        #print(guess)
        if key==guess:
            return mid
        elif key<guess:
            high=mid-1
        elif key>guess:
            low=mid+1
        #print(low,high)
    return "Not Found"
array=[1,2,3,4,5,6,7,8,9]
key=91
print(bs(array,key))