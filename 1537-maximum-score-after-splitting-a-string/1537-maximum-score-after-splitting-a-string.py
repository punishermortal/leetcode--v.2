class Solution:
    def maxScore(self, s: str) -> int:
        res = 0
        for i in range(1,len(s)):
            res_lef = s[:i].count("0")
            res_right = s[i:].count("1")
            res =max(res,(res_lef + res_right))
        return res
        