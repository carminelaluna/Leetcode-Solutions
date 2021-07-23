class Solution:
     
    
    def rob(self, nums: List[int]) -> int:
        
        def res(nums):
            app = [0] * len(nums)
            app[0] = nums[0]
            app[1] = max(nums[0],nums[1])
            for i in range(2,len(nums)):
                app[i] = max(app[i-1],nums[i]+app[i-2])
            return max(app[len(app)-1],app[len(app)-2])
        
        if len(nums) == 2:
            return max(nums[0],nums[1])
        if len(nums) == 1:
            return nums[0]
        else:
            if len(nums) == 0:
                return 0
        return max(res(nums[1:]),res(nums[:-1]))
        
