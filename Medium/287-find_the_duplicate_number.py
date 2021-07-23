class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ptr = nums[0]
        ptr2 = nums[0]
        while True:
            ptr = nums[ptr]
            ptr2 = nums[nums[ptr2]]
            if ptr == ptr2:
                break
        tmp = nums[0]
        app = ptr
        while tmp != app:
            tmp = nums[tmp]
            app = nums[app]
        return tmp
