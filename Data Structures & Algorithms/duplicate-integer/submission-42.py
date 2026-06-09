class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap={}
        for i in range(len(nums)):
            if nums[i] in hmap:
                hmap[nums[i]]+=1
            else:
                hmap[nums[i]]=1
        for v in hmap.values():
            if v>1:
                return True
        return False