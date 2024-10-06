class Solution:
    def areSentencesSimilar(self,*q) -> bool:
        return (f:=lambda q:sum(takewhile(int,map(eq,*q))))(q:=[*map(str.split,q)])+f(map(reversed,q))>=min(map(len,q))