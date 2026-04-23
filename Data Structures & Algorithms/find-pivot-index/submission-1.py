class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        left=0
        for i,val in enumerate(nums):
            if left==total-left-val:
                return i
            left+=val
        return-1