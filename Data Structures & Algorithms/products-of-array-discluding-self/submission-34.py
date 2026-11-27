class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*len(nums)
        lp=1
        rp=1
        for i in range(1,len(nums)):
            lp=res[i-1]*nums[i-1]
            res[i]*=lp
        for j in range(len(nums)-2,-1,-1):
            rp*=nums[j+1]
            res[j]*=rp
        return res
            
