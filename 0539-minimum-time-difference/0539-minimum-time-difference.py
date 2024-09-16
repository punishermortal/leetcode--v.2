class Solution:
    def findMinDifference(self, t: List[str]) -> int:
        tab=[]
        for i in t:
            tab.append(int(i[0:2])*60+int(i[3:]))
        tab.sort()
        n=len(tab)
        res=1440+tab[0]-tab[n-1]
        for i in range(1,n):
            res=min(res,(tab[i]-tab[i-1]))
        return res    