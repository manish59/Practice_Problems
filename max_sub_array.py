def max_sub_array(array):
    local=float("-inf")
    global_=float("-inf")
    for i in range(0,len(array)):
        print("Before:",local)
        local=max(local,array[i]+local)
        #print("After:",local)
        #if local>global_:
        #    global_=local
#kandane algorithm
array=[-2,1,-3,4,-1,2,1,-5,4]
print(max_sub_array(array))