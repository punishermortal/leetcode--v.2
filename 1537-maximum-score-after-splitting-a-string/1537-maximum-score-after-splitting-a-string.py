class Solution:
    def maxScore(self, s: str) -> int:
        zero=0
        ones=0
        if s[0]=="0":
            zero+=1
        for i in range(1,len(s)):
            if s[i]=="1":
                ones+=1
        maxi=zero+ones
        for i in range(1,len(s)-1):
            if s[i]=="1":
                ones-=1
            else:
                zero+=1
            maxi=max(maxi,ones+zero)
        return maxi