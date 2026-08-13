class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        s=0
        for i in num1:
            r=ord(i)-ord('0')
            s=s*10+r
        x=s
        s=0
        for i in num2:
            r=ord(i)-ord('0')
            s=s*10+r
        y=s
        return str(x*y)