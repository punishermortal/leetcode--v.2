class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        return (f:=reduce(or_, map(Counter, words2))) and [w for w in words1 if Counter(w)>=f]
        res=[]
        for s in words1:
            flag =True
            for i in words2:
                if i not in s:
                    flag =False
                    break
            if flag:
                res.append(s)
        return res


