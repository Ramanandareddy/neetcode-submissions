class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp=float('-inf')
        cp=prices[0]
        for i in range(len(prices)):
            cp=min(prices[i],cp)
            p=prices[i]-cp 
            print(p)
            mp=max(mp,p)
            print(mp)
            
            print(cp)
        return mp
        
            
        