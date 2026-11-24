class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp=Counter(nums)
        heap=[]
        for key,val in mp.items():
           
            if len(heap)<k:
                heapq.heappush(heap,(val,key))
            else:
                heapq.heappushpop(heap,(val,key))
        
        return [h[1] for h in heap]
        