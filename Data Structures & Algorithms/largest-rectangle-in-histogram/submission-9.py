class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area=0
        st=[]
        for i,a in enumerate(heights):
            res=i
            while st and st[-1][0]>=a:
                h,ind=st.pop()
                area=max(area,h*(i-ind))
                res=ind
            st.append((a,res))
        print(st)
        while st:
            h,ind=st.pop()
            area=max(area,h*(len(heights)-ind))
            print(area)
        return area