class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        ans = ""
        counter = 0
        for i in range(len(s)):
            if counter < len(spaces) and i == spaces[counter]:
                res = res + ans + " "
                ans = ""
                counter += 1
            ans = ans + s[i]
        return res+ans
        