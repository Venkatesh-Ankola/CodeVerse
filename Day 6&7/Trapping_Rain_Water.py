class Solution:
    def trap(self, height: List[int]) -> int:
        f = 0
        l = len(height)-1
        res = 0
        cur = 0
        fm = height[f]
        lm = height[l]

        while f<l:
            if height[l] > height[f]:
                f+=1
                fm = max(fm,height[f])
                cur += fm - height[f]

            else:
                l-=1
                lm = max(lm,height[l])
                cur += lm - height[l]

        return cur
        