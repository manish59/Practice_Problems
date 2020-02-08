class Solution:
    def romanToInt(self,s):
        result_number=0
        roman_mapping={'I':1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        i=0
        while(i<len(s)):
            #print('Index',i)
            if i!=len(s)-1:
                if (s[i]=="I" and s[i+1]=="V") or \
                        (s[i]=="I" and s[i+1]=="X") or \
                        (s[i]=="X" and s[i+1]=="L") or \
                        (s[i]=="X" and s[i+1]=="C") or \
                        (s[i]=="C" and s[i+1]=="D") or \
                        (s[i]=="C" and s[i+1]=="M") :
                        result_number=result_number+roman_mapping[s[i+1]]-roman_mapping[s[i]]
                        i=i+1
                else:
                    result_number=result_number+roman_mapping[s[i]]
            else:
                result_number=result_number+roman_mapping[s[i]]
            i=i+1
            #print(result_number)
        return result_number 
print(Solution().romanToInt("LVIII"))
        