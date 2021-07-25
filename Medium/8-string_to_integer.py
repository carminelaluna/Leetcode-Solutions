class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.lstrip()
        if len(s)==0: 
            return 0
        sign = 1
        if s[0] in ['+','-']: 
            sign = int(f"{s[0]}1")
            s = s[1:]
        app = ""  
        for i in s:
            try:
                if int(i) >= 0 and int(i) <= 9:
                    app+=i
                    break
            except:
                break
        if len(app) == 0:
            return 0
        if sign > 0:
            return min(int(app) * sign, 2**31-1)
        else:
            return max(int(app) *sign, -2**31)
