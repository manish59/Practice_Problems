def binary_search(arr,l,r,key):
    if l<=r:
        mid=int((l+r)/2)
        if arr[mid]==key:
            return "True"
        elif key<arr[mid]:
            return binary_search(arr,l,mid-1,key)
        elif key>arr[mid]:
            return binary_search(arr,mid+1,r,key)
    else:
        return "Not Found"
print(binary_search([1,2,3,4,5,6],0,5,8))