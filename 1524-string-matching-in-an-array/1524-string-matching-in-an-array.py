class Solution:
    def checker(self,arr:List[str],s:str)->bool:
        for word in arr:
            if len(word)>len(s):
                for i in range(len(word)):
                    if word[i:].startswith(s):
                        return True
        return False

    def stringMatching(self, words: List[str]) -> List[str]:
        res=[]
        for s in words:
            if self.checker(words,s):
                res.append(s)
        return res