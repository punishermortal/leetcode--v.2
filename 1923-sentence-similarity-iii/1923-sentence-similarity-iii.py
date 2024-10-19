class Solution:

    def toStringVec(s: str):
        return s.split()


    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = Solution.toStringVec(sentence1)
        s2 = Solution.toStringVec(sentence2)
        
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            s1, s2 = s2, s1
            n1, n2 = n2, n1
        
        l = 0
        r1, r2 = n1 - 1, n2 - 1

        while l < n1 and s1[l] == s2[l]:
            l += 1

        while r1 >= 0 and s1[r1] == s2[r2]:
            r1 -= 1
            r2 -= 1
        return r1 < l