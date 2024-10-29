class Solution(object):
    def minAddToMakeValid(self, s):
        open_brackets = 0
        mismatch = 0
        for char in s:
            if char == '(':
                open_brackets += 1
            else:
                if open_brackets > 0:
                    open_brackets -= 1
                else:
                    mismatch += 1
        return open_brackets + mismatch