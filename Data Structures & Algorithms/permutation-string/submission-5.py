class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1freq=Counter(s1)
        need=len(s1freq)
        for i in range(len(s2)):
            count2={}
            cur=0 
            for j in range(i,len(s2)):
                count2[s2[j]]=1+count2.get(s2[j],0)
                if s1freq.get(s2[j],0)<count2[s2[j]]:
                    break
                if s1freq.get(s2[j],0)==count2[s2[j]]:
                    cur+=1
                if cur==need:
                    return True
        return False

                