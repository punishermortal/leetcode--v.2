class Solution:
    def solve(self , s :str):
        res=[]
        for i in range(len(s)):
            if s[i] == '+' or s[i] == '-' or s[i] == '*':
                left_arr = self.solve(s[:i])
                right_arr = self.solve(s[i+1:])
                for x in left_arr:
                    for y in right_arr:
                        if(s[i] == '+'):
                            res.append(int(x)+int(y))
                        elif(s[i] == '-'):
                            res.append(int(x)-int(y))
                        else:
                            res.append(int(x)*int(y))
        if(len(res) == 0):
            return [int(s)]
        return res
    def solve(self, s: str, memo: dict) -> List[int]:
        if s in memo:
            return memo[s]
        
        res = []
        for i in range(len(s)):
            if s[i] in '+-*':
                left_arr = self.solve(s[:i], memo)
                right_arr = self.solve(s[i+1:], memo)
                for x in left_arr:
                    for y in right_arr:
                        if s[i] == '+':
                            res.append(x + y)
                        elif s[i] == '-':
                            res.append(x - y)
                        elif s[i] == '*':
                            res.append(x * y)
        if not res:
            res = [int(s)]
        memo[s] = res
        return res


    def diffWaysToCompute(self, expression: str) -> List[int]:
        # return self.solve(expression)
        memo = {}
        return self.solve(expression, memo)

