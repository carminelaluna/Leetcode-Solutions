class Solution:
    def mySqrt(self, x: int) -> int:
        n = 1
        if x == 0 :
            return 0
        if x == 2 or x == 1:
            return 1
        for i in range(0,x):
            if i * i > x:
                return i-1
            else:
                if i * i == x:
                    return i
