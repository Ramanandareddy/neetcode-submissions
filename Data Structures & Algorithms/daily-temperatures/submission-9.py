class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st=[]
        res=[0]*len(temperatures)
        for i,a in enumerate(temperatures):
            while st and st[-1][0]<a:
                temp,ind=st.pop()
                res[ind]=i-ind
            st.append((a,i))
        return res