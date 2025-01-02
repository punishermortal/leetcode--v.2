class Solution:
    def compressedString(self, word: str) -> str:
        res = []
        n = len(word)
        i = 0
        while i < n:
            ls = word[i]
            count = 1
            while i + count < n and word[i + count] == ls and count < 9:
                count += 1
            res.append(str(count) + ls)
            i += count
        return ''.join(res)