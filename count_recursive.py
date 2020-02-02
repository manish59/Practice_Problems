def count(a):
    result=0
    if len(a)==1:
        return 1
    else:
        return 1+count(a[:len(a)-1]) 
print(count([1,2,3,4,5,6,7]))