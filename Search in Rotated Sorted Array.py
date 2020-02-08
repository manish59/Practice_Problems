class Solution:
    def search(self,array,target):
        self.array=array
        self.target=target
        print(self.array,self.target)
        pivot=self.find_rotate_index()
        #print(pivot)
        index=0
        if pivot==0:
            #("First if")
            index=self.binary_search(self.array,self.target)
        elif self.target>self.array[0]:
            print("Target is greater than pivot element")
            index=self.binary_search(self.array[:pivot],self.target)
            print("Index:",index)
            #print(index)
        elif self.target==self.array[pivot]:
            return pivot
        elif self.target<self.array[0]:
            print("Target is less than pivot element")
            index=self.binary_search(self.array[pivot:],self.target)
            if index!="-1":
                index=pivot+index
        return index
    def binary_search(self,array,target):
        low=0
        high=len(array)-1
        while(low<=high):
            mid=int((low+high)/2)
            #print(low,mid)
            guess=array[mid]
            if target==guess:
                return mid
            elif target<guess:
                high=mid-1
            elif target>guess:
                low=mid+1
        return "-1"
    def find_rotate_index(self):
        i=0
        #print("Find Pivort Rotate Index funcation Called",i)
        while(i<len(self.array)-1):
            #print(self.array[i])
            if self.array[i]>self.array[i+1]:
                return i+1
            i=i+1
        return 0
array=[3,1]
target=3
print("Index",Solution().search(array,target))
array=[4,5,6,7,0,1,2]
target=2
print("Index",Solution().search(array,target))
array=[4,5,6,7,0,1,2]
target=0
print("Index",Solution().search(array,target))
array=[4,3,5,6,7]
target=7
print("Index",Solution().search(array,target))