# 先排序，再逐个对比
# TC:O(n*logn), SC:O(1)

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums.sort()
        pre = nums[0]

        for i in range(1, len(nums)):
            if pre == nums[i]:
                return pre 

            pre = nums[i]