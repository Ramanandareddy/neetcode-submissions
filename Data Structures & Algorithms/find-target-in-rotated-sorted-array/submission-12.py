class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findmin(nums):
            l=0
            r=len(nums)-1
            while l<r:
                m=(l+r)//2
                if nums[m]>nums[r]:
                    l=m+1
                else:
                    r=m
            return l
        def binarysearch(nums,target):
            l=0
            r=len(nums)-1
            while l<=r:
                m=(l+r)//2
                if nums[m]==target:
                    return m
                elif nums[m]<target:
                    l=m+1
                else:
                    r=m-1
            return -1
        ind=findmin(nums)
        fst=binarysearch(nums[:ind],target)
        sec=binarysearch(nums[ind:],target)
        if fst==sec==-1:
            return -1
        elif fst!=-1:
            return fst
        elif sec!=-1:
            return sec+ind
        
        
