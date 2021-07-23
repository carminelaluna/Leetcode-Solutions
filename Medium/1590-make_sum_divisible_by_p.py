class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        s = sum(nums)%p
        if s == 0:
            return 0
        res = math.inf
        hmap = {0:-1}
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            tmp = curr % p
            if (tmp -s) % p in hmap:
                res = min(res, i-hmap[(tmp-s)%p])
            hmap[tmp] = i
        if res < len(nums):
            return res
        else:
            return -1class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        s = sum(nums)%p
        if s == 0:
            return 0
        res = math.inf
        hmap = {0:-1}
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            tmp = curr % p
            if (tmp -s) % p in hmap:
                res = min(res, i-hmap[(tmp-s)%p])
            hmap[tmp] = i
        if res < len(nums):
            return res
        else:
            return -1
