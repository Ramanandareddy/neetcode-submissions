class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        maxwindow=0
        freqmap={}
        for r in range(len(s)):
            freqmap[s[r]]=1+freqmap.get(s[r],0)
            while (r-l+1)-max(freqmap.values())>k:
                freqmap[s[l]]-=1
                l+=1
            maxwindow=max(maxwindow,r-l+1)
            
        return maxwindow