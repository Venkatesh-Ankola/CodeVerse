class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        su =0
        i =0
        while i < len(s)-1:
            if dic[s[i+1]]>dic[s[i]]:
                su = su - (dic[s[i]] )
                i+=1
            else:
                su +=dic[s[i]]
                i+=1

        return su+dic[s[-1]]
        