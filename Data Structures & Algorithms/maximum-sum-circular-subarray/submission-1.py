class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curmax,curmin=0,0
        globmax,globmin=nums[0],nums[0]
        total=0
        for n in nums:
            curmax,curmin=max(curmax+n,n),min(curmin+n,n)
            globmax,globmin=max(curmax,globmax),min(curmin,globmin)
            total+=n
        return max(globmax,total-globmin) if globmax>0 else globmax