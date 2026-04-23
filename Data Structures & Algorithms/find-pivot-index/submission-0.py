class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prs=[]
        pos=[]
        s=0
        for i in range(len(nums)):
            s+=nums[i]
            prs.append(s)
        s=0
        for i in range(len(nums)-1,-1,-1):
            s+=nums[i]
            pos.append(s)
        print(prs,pos)
        pos.reverse()
        for i in range(len(nums)):
            if prs[i]==pos[i]:
                return i
        
        return -1


