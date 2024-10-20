from collections import deque

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        operator = deque()
        parenthesis = deque()
        for i in expression:
            if i in "!&|": operator.append(i)
            elif i == ',': continue
            elif i not in ")": parenthesis.append(i)
            else:
                last_operator = operator.pop()
                last_express  = parenthesis.pop()
                last_express = True if last_express=='t' else False
                if last_operator=='&':
                    while parenthesis[-1]!='(':
                        temp = True if parenthesis.pop()=='t' else False
                        last_express = last_express and temp
                elif last_operator=='!':
                    last_express = not last_express
                elif last_operator=='|':
                    while parenthesis[-1]!='(':
                        temp = True if parenthesis.pop()=='t' else False
                        last_express = last_express or temp
                parenthesis.pop()
                temp = 't' if last_express else 'f'
                parenthesis.append(temp)
        return last_express                