class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(i,curlist,total):
            if total==target:
                res.append(curlist.copy())
                return
            if i>=len(nums) or total>target:
                return
            curlist.append(nums[i])
            dfs(i,curlist,total+nums[i])
            curlist.pop()
            dfs(i+1,curlist,total) 
        dfs(0,[],0)
        return res
         