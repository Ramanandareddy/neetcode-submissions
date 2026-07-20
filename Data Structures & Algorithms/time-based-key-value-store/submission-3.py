class TimeMap:

    def __init__(self):
        self.mp=defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        l=self.mp.get(key,[])
        ll=0
        r=len(l)-1
        res=''
        while ll<=r:
            m=(ll+r)//2
            if l[m][1]<=timestamp:
                res=l[m][0]
                ll=m+1
            else:
                r=m-1
        return res