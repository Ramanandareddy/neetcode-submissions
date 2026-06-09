class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*len(nums)
        lp=1
        rp=1
        for i in range(1,len(nums)):
            lp*=nums[i-1]                #[1,1,2,8]
            res[i]*=lp
        for i in range(len(nums)-2,-1,-1):
            rp*=nums[i+1]
            res[i]*=rp
        return res
