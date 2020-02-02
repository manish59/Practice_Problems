def qsort(array):
    if len(array)<2:
        return array
    else:
        pivot=array[0]
        less=[i for i in array[1:] if i<=pivot]
        great=[i for i in array[:1] if i>pivot]
        print(less,great)
        return qsort(less)+[pivot]+qsort(great)
print(qsort([10,9,8,7,4,312,123]))