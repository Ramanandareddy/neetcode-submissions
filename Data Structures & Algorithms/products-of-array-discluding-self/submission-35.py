class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*len(nums)
        lp=[1]*len(nums)
        rp=[1]*len(nums)
        for i in range(1,len(nums)):
            lp[i]=lp[i-1]*nums[i-1]
        for j in range(len(nums)-2,-1,-1):
            rp[j]=rp[j+1]*nums[j+1]
        for k in range(len(nums)):
            res[k]=lp[k]*rp[k]
        return res