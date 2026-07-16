class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l=0
        r=len(height)-1
        lm=height[l]
        rm=height[r]

        area=0
        while l<r:
            if lm<=rm:
                l+=1
                lm=max(height[l],lm)
                area+=height[l]-lm
                
            else:
                r-=1
                rm=max(height[r],rm)
                area+=height[r]-rm
                
        return area*-1
