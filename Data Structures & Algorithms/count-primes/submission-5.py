class Solution:
    def countPrimes(self, n: int) -> int:
        seive=[False]*n
        res=0
        for i in range(2,n):
            if not seive[i]:
                res+=1
                for j in range(i,n,i):
                    seive[j]=True
        return res