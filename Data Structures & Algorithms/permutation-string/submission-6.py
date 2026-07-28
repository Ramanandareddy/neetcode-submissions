class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1count=Counter(s1)
        need=len(s1count)
        for i in range(len(s2)):
            s2count,cur={},0
            for j in range(i,len(s2)):
                s2count[s2[j]]=1+s2count.get(s2[j],0)
                if s1count.get(s2[j],0)<s2count[s2[j]]:
                    break
                if s1count.get(s2[j],0)==s2count[s2[j]]:
                    cur+=1
                if need==cur:
                    return True
        return False
