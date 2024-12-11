class Solution:
    def maximumLength(self, s: str) -> int:
        hm = {}
        n = len(s)
        for i in range(n):
            substr = ""
            for j in range(i,n):
                if len(substr) == 0 or substr[-1] == s[j]:
                    substr += s[j]
                    hm[substr] = hm.get(substr)+1 if substr in hm else 1
                else:
                    break
        res = -1
        for st in hm.keys():
            if len(st)>res and hm.get(st)>2:
                res = len(st)
        return res