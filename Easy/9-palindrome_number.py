class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        y="".join(reversed(x))
        if(y==x):
            return True
        else:
            return False
