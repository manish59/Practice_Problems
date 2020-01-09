def hourglassSum(arr):
    sum_list_hour_glass=[]
    for i in range(len(arr)-2):
            for j in range(0,3):
                    #print(arr[i],arr[i+1],arr[i+2])
                    sum=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
                    #print(sum)
                    sum_list_hour_glass.append(sum)
    return max(sum_list_hour_glass)
if __name__ == "__main__":
    arr=[[1, 1, 1, 0, 0, 0], 
         [0, 1, 0, 0, 0, 0], 
         [1, 1, 1, 0, 0, 0], 
         [0, 0, 2, 4, 4, 0], 
         [0, 0, 0, 2, 0, 0], 
         [0, 0, 1, 2, 4, 0]]    
    hourglassSum(arr)