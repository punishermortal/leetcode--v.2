class Solution:
    def maximumLength(self, s: str) -> int:
        hsh={}
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if s[i:j] in hsh.keys() :
                    hsh[s[i:j]]+=1
                else:
                    hsh[s[i:j]]=1
        mx=-1
        for i in hsh.keys():
            if hsh[i]>=3 and len(i)>mx and len(set(i))==1:
                mx=len(i)
        return(mx)