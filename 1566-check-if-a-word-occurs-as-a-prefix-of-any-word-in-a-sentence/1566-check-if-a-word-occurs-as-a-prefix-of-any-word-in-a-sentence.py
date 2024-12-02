class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        count = 0
        for i in (sentence.split(" ")):
            count += 1
            if i.startswith(searchWord):
                return count
        return -1
        