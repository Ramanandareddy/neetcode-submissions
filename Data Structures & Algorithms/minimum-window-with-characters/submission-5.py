class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=='':
            return ''
        s2counter=Counter(t)
        have=0
        need=len(s2counter)
        l=0
        window={}
        reslen=float('inf')
        res=[-1,-1]
        for r in range(len(s)):
            window[s[r]]=1+window.get(s[r],0)
            if s[r] in s2counter and s2counter[s[r]]==window[s[r]]:
                have+=1
            while have==need:
                if r-l+1<reslen:
                    reslen,res=min(reslen,r-l+1),[l,r]
                window[s[l]]-=1
                if s[l] in s2counter and s2counter[s[l]]>window[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if reslen!=float('inf') else ''