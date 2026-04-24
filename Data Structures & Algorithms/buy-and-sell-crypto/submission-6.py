class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp=float('-inf')
        cp=prices[0]
        for i in range(len(prices)):
            p=prices[i]-cp 
            print(p)
            mp=max(mp,p)
            print(mp)
            cp=min(prices[i],cp)
            print(cp)
        return mp
        
            
        