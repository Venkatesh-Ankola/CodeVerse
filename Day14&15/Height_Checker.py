class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        exp = []
        for n in heights:
            exp.append(n)
        
        exp.sort()
        cnt =0
        for i in range(len(heights)):
            if exp[i]!=heights[i]:
                cnt+=1

        return cnt
        