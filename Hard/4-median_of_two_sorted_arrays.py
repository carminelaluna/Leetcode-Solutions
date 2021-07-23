class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        summ = 0
        Num = nums1 + nums2
        Num.sort()
        if len(Num) %2==1:
            return Num[int(len(Num)/2)]
        else:
            return (Num[int(len(Num)/2-1)] + Num[int(len(Num)/2)] )/2
