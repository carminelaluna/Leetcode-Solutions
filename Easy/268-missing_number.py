class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i-1] != nums[i] -1:
                return i
        if nums[0] == 0:
            return nums[len(nums)-1] + 1
        else:
            return 0
