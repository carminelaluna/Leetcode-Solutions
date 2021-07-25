class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
                return s
        res = ["" for _ in range(numRows)]
        for i in range(len(s)):
            tmp = i % (2*numRows-2)
            if tmp < numRows:
                res[tmp] += s[i]
            else:
                res[numRows-tmp-2] += s[i]
        return "".join(res)
