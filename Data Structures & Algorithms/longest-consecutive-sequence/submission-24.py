class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        
        maxl=float('-inf')
        for i in numset:
            if i-1 not in numset:
                l=0
                while i+l in numset:
                    l+=1
                maxl=max(maxl,l)
        return maxl if maxl!=float('-inf') else 0
                
