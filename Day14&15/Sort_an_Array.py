class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
    
        n = len(nums)
        if n < 2:
            return nums[:]
        else:
            middle = n//2
            l = self.sortArray(nums[:middle])
            r = self.sortArray(nums[middle:])
            return self.merge(l,r)

    def merge(self,l,r):
        res = []
        i,j=0,0
        while i<len(l) and j<len(r):
            if l[i]< r[j]:
                res.append(l[i])
                i+=1
            else:
                res.append(r[j])
                j+=1

        while i < len(l):
            res.append(l[i])
            i += 1
        while j < len(r):
            res.append(r[j])
            j += 1
        return res

        