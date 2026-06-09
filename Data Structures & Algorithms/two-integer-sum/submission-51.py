class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp={}
        for i,a in enumerate(nums):
            if target-a in mp:
                return [mp[target-a],i]
            mp[nums[i]]=i
        return [-1]*2