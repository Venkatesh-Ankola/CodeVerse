class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        ele = nums[0]

        for n in nums:
            if count == 0:
                ele = n
                count +=1
            elif n == ele:
                count +=1
            else:
                count -=1

        return ele
        