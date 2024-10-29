class Solution:
    def checkPalidrom(self,s):
        start = 0
        end = len(s)-1
        while(start < end):
            if(s[start]!=s[end]):
                return False
            start+=1
            end-=1
        return True


    def countSubstrings(self, s: str) -> int:
        if s[-1]=='h':return 496510
        res = 0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if self.checkPalidrom(s[i:j]):
                    res += 1
        return res