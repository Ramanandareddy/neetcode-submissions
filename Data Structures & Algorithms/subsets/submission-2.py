class Solution:
    def helper(self,i,curset,subset,nums):
        if i>=len(nums):
            subset.append(curset.copy())
            return
        curset.append(nums[i])
        self.helper(i+1,curset,subset,nums)
        curset.pop()
        self.helper(i+1,curset,subset,nums)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curset,subset=[],[]
        self.helper(0,curset,subset,nums)
        return subset

        
