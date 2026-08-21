class Solution:
    def helper(self,i,curset,subset,nums):
        nums.sort()
        if i>=len(nums):
            subset.append(curset.copy())
            return
        curset.append(nums[i])
        self.helper(i+1,curset,subset,nums)
        curset.pop()
        while i+1<len(nums) and nums[i]==nums[i+1]:
            i+=1
        self.helper(i+1,curset,subset,nums)
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        curset,subset=[],[]
        self.helper(0,curset,subset,nums)
        return subset