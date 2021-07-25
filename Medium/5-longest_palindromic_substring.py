class Solution:
    def longestPalindrome(self, s: str) -> str:
        tmp = ""
        max_palindrome = ""
        for i in range(len(s)):
            tmp += s[i]
            for j in range(len(tmp)):
                if tmp[j] == s[i] and s[j:i+1] == s[j:i+1][::-1] and len(s[j:i+1]) > len(max_palindrome):
                     max_palindrome = s[j:i+1]
                     break                                                                                                      return max_palindrome                                                                                                                                        
