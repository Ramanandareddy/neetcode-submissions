class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        opn,cln=0,0
        res=[]
        st=[]
        def backtrack(opn,cln):
            if opn==cln==n:
                res.append(''.join(st))
                return
            if opn<n:
                st.append('(')
                backtrack(opn+1,cln)
                st.pop()
            if cln<opn:
                st.append(')')
                backtrack(opn,cln+1)
                st.pop()
        backtrack(0,0)
        return res
