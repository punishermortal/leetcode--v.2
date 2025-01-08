class Solution:
    def isPrefixAndSuffix(self,s1:str ,s2:str)->bool:
        if s2.startswith(s1) and s2.endswith(s1):
            return True
        return False

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count =0
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                if self.isPrefixAndSuffix(words[i],words[j]):
                    count+=1
        return count
        