class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        lm=height[l]
        rm=height[r]
        area=0
        while l<r:
            if lm<=rm:
                l+=1
                lm=max(height[l],lm)
                area+=lm-height[l]
            else:
                r-=1
                rm=max(rm,height[r])
                area+=rm-height[r]
        return area