class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        max_l = nums[0]
        max_succ = 0
        res = 0
        for i in range(1,len(nums)):
            if nums[i] > max_succ:
                max_succ = nums[i]
            if nums[i] < max_l:
                res = i
                if max_succ > max_l:
                    max_l = max_succ
        return res + 1
                
