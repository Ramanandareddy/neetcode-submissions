class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp=Counter(nums)
        freq=[[] for i in range(len(nums)+1)]
        for key,v in mp.items():
            freq[v].append(key)
        res=[]
        
        res=[]
        for i in range(len(nums),0,-1):
            for j in freq[i]:
               
                res.append(j)
                if len(res)>=k:
                    return res
                
        return [-1]