class Solution:
    def isValid(self, s: str) -> bool:
        mp={
            ']':'[',
            '}':'{',
            ')':'('
        }
        st=[]
        for i in s:
            if i in mp.values():
                st.append(i)
            elif i in mp.keys() and st and st[-1]==mp[i]:
                st.pop()
            else:
                return False
        return True if not st else False