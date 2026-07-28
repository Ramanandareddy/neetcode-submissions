class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        res=0
        count=0
        mp=defaultdict(int)
        for r in range(len(s)):
            mp[s[r]]=1+mp.get(s[r],0)
            count=max(count,mp[s[r]])
            if (r-l+1)-count>k:
                mp[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res
            