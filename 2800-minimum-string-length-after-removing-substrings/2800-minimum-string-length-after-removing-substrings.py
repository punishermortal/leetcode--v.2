class Solution:
    def minLength(self, s: str) -> int:
        i=0#"AB FCACDB"
        count=0
        while(i<len(s)-1):
            print(s,len(s),i)
            if s[i:].startswith("AB") or s[i:].startswith("CD"):
                s = s[:i]+s[i+2:]
                print(s,"q")
                count+=1
                if(i>0):i-=1
            else:
                i+=1
        return len(s)