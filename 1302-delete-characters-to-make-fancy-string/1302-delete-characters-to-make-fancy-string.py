class Solution:
    def makeFancyString(self, s: str) -> str:
         
        for ch in set(s):                       
            while s.find(ch*10) != -1: s = s.replace(ch*10, ch*2)
            s = s.replace(ch*6, ch*2).replace(ch*4, ch*2).replace(ch*3, ch*2) 
               
        return s