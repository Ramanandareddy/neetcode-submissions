class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        counter=Counter(nums)
        for key,v in counter.items():
            if k>len(heap):
                heapq.heappush(heap,(v,key))
            else:
                heapq.heappushpop(heap,(v,key))
        print(heap)
        return list(i[1] for i in heap)
        