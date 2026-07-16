class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res=[(pos,sp) for pos,sp in zip(position,speed)]
        st=[]
        res.sort()
        for pos,sp in res[::-1]:
            tt=(target-pos)/sp
            st.append(tt)
            while len(st)>=2 and st[-1]<=st[-2]:
                st.pop()
            
            
            
        return len(st)
