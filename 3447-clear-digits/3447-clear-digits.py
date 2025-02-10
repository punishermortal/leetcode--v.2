class Solution:
    def clearDigits(self, s: str) -> str:
        ls=[]
        for i in range(len(s)):
            if s[i].isdigit():
                ls.pop()
            else:
                ls.append(s[i])
        return ''.join(ls)
        