class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter=Counter(nums)
        freq=[[]for i in range(len(nums)+1)]
        print(freq)
        for key,val in counter.items():
            freq[val].append(key)
        print(freq)
        res=[]
        for i in range(len(freq)-1,0,-1):
            for val in freq[i]:
                if len(res)<k:
                    res.append(val)
    

        return res