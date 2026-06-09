class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        freq=[[] for i in range(len(nums)+1)]
        print(freq)
        for key,val in count.items():
            freq[val].append(key)
        print(freq)
        res=[]
        for i in range(len(nums),0,-1):
            for j in freq[i]:
                if len(res)==k:
                    return res
                res.append(j)


        return res