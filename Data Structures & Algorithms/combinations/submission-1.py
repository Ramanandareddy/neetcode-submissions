class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(i,curcomb,comb,n,k):
            if len(curcomb)==k:
                comb.append(curcomb.copy())
                return
            if i>n:
                return
            curcomb.append(i)
            helper(i+1,curcomb,comb,n,k)
            curcomb.pop()
            helper(i+1,curcomb,comb,n,k)
        comb=[]
        helper(1,[],comb,n,k)
        return comb
