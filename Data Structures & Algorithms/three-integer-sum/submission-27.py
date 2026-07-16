class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i , a in enumerate(nums):
            if a>0:
                break
            if i>0 and nums[i-1]==a:
                continue
            j=i+1
            k=len(nums)-1
            while j<k:
                if a+nums[j]+nums[k]<0:
                    j+=1
                elif a+nums[j]+nums[k]>0:
                    k-=1
                else:
                    res.append([a,nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j-1]==nums[j]:
                        j+=1
        return res
