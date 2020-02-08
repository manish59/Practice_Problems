class Solution:
    def __init__(self):
        self.mapper={"(":")","{":"}","[":"]"}
        #print(self.mapper)
    def isValid(self,s):
        result=[]
        for i in s:
            print(i)
            if i in self.mapper:
                result.append(i)
            else:
                if len(result)>0:
                    if self.mapper[result.pop()]==i:
                        continue
                return False
            print(result)
        if len(result)<=0:
            return True
        else:
            return False


print(Solution().isValid("}"))