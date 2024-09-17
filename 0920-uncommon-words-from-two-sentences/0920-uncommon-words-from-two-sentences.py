class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1dic = {item: s1.split(" ").count(item) for item in set(s1.split(" "))}
        s2dic = {item: s2.split(" ").count(item) for item in set(s2.split(" "))}
        res=[key for key,value in s1dic.items() if key not in s2dic and s1dic[key]<2]
        ans=[key  for key,value in s2dic.items() if key not in s1dic and s2dic[key]<2]
        return res+ans

        
