class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        cnt=1
        res1 = 1
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]+1:
                cnt+=1 
            else:
                cnt = 1

            res1 = max(res1,cnt)
        nums.sort()
        print(nums)
        cnt = 1
        res = 1
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]+1:
                cnt+=1 
            elif nums[i+1] == nums[i]:
                continue
            else:
                cnt = 1

            res = max(res,cnt)

        return max(res,res1)
        