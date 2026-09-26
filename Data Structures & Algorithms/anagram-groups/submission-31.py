class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        hm={}
        for w in strs:
            counter=[0]*26
            
            for l in w:
                counter[ord(l)-ord('a')]+=1
            if tuple(counter) not in hm:
                hm[tuple(counter)]=[]
            hm[tuple(counter)].append(w)
        return list(hm.values())