class Solution:
    def addZero(self,num):
        while(len(num)<4):
            num="0"+num
        return num
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        num1=self.addZero(str(num1))
        num2=self.addZero(str(num2))
        num3=self.addZero(str(num3))
        res=sorted(num1[0] + num2[0] + num3[0])[0] + sorted(num1[1] + num2[1] + num3[1])[0] + sorted(num1[2] + num2[2] + num3[2])[0] + sorted(num1[3] + num2[3] + num3[3])[0]
        return int(res) 