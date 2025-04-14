class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = {}
        for i in range(len(nums)):
            if nums[i] in cnt.keys():
                cnt[nums[i]] +=1
            else:
                cnt[nums[i]] =1

        i = 0

        for j in range(3):
            f = cnt.get(j,0)
            nums[i:i+f] = [j]*f
            i +=f        