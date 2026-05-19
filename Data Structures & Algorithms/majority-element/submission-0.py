import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cmap=Counter(nums)
        val=0
        for k,v in cmap.items():
            if v>math.floor(len(nums)/2):
                val=k
        return val