class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sumlist=[]
        def helper(i,curlist,total):
            if total==target:
                sumlist.append(curlist.copy())
                return
            if i>=len(nums)or total > target:
                return
            curlist.append(nums[i])
            helper(i,curlist,total+nums[i])
            curlist.pop()
            helper(i+1,curlist,total)
        helper(0,[],0)
        return sumlist

            