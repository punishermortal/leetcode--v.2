class Solution:
    def minimumSteps(self, s: str) -> int:
        res = 0
        black = 0
        for ch in  s:
            if ch == '1':
                black += 1
            else:
                res += black
        return res

# logic is that have to be remebemer how many 1 are in past till o will get
