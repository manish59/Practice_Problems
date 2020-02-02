def Selection_Sort(arr):
    for i in range(0,len(arr)-1):
        min=i
        for j in range(i+1,len(arr)): # here the range tells us which part of the list is sorted and which part of the list is not sorted by depending the index from the outer loop
            if arr[j]<arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
    return arr
if __name__=="__main__":
    arr=[98,78,34,21,12,32,45,43]
    print(Selection_Sort(arr))