class Stack:
    def __init__(self):
        self.stack =[]
        # return self.stack
    
    def top(self):
        if len(self.stack)>0:
            return self.stack[-1]
        else:
            return "opps stack is empty"

    def length_st(self):
        return len(self.stack)

    def push(self,val):
        self.stack.append(val)
        
    def pop(self):
        if len(self.stack)>0:
            return self.stack.pop()
        else:
            return "opps stack is empty"

class Solution:
    def minSwaps(self, s: str) -> int:
        st = Stack()
        for i in range(len(s)):
            if s[i]=="[":
                st.push(s[i])
            else:
                if st.length_st()>0:
                    st.pop()
        return (st.length_st()+1)//2
        