class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        res=r
        while l<=r:
            m=(l+r)//2
            tt=0
            tt=sum(math.ceil(i/m) for i in piles)
            if tt<=h:
                res=m
                r=m-1
            else:
                l=m+1
        return res

                