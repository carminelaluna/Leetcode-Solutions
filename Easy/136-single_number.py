class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        print(n)
        for i in range(1,n,2):
            if not nums[i] == nums[i-1]:
                return nums[i-1]
        return nums[-1]
