class Solution:
    def minLength(self, s: str) -> int:
        i,count=0,0
        while(i<len(s)-1):
            if s[i:].startswith("AB") or s[i:].startswith("CD"):
                s = s[:i]+s[i+2:]
                count+=1
                if(i>0):i-=1
            else:
                i+=1
        return len(s)