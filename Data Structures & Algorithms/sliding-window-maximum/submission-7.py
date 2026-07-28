class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        l=0
        for i in range(len(nums)-k+1):
            res.append(max(nums[l:k+i]))
            l+=1
        return res