class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cp=float('inf')
        mp=float('-inf')
        for p in prices:
            cp=min(cp,p)
            pr=p-cp
            mp=max(mp,pr)
        return mp