class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = ""
        maxV = -1
        conta = 0
        i = 0
        while i <  (len(s)):	
            if s[i] not in temp:
                temp += s[i]
            else:
                reset = True
                if maxV < len(temp):
                    maxV = len(temp)
                conta +=1
                i = conta -1 
                temp = ""
            i+=1
        if maxV < len(temp):
            maxV = len(temp)
            
        return maxV
