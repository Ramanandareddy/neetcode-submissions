class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp=float('-inf')
        cp=float('inf')
        for i in range(len(prices)):
            cp=min(prices[i],cp)
            mp=max(mp,prices[i]-cp)
        return mp
        
            
        