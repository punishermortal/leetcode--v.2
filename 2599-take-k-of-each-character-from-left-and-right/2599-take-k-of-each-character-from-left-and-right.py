class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        left, right = 0, 0
        ans = n
        count_a, count_b, count_c = 0, 0, 0
        totalA, totalB, totalC = s.count('a'), s.count('b'), s.count('c')
        if totalA < k or totalB < k or totalC < k:
            return -1

        while right < n:
            if s[right] == 'a': 
                count_a += 1
            if s[right] == 'b': 
                count_b += 1
            if s[right] == 'c': 
                count_c += 1
            right += 1
            while count_a > totalA - k or count_b > totalB - k or count_c > totalC - k:
                if s[left] == 'a': 
                    count_a -= 1
                if s[left] == 'b': 
                    count_b -= 1
                if s[left] == 'c': 
                    count_c -= 1
                left += 1
            ans = min(ans, n - (right - left))
        return ans