class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s=0
        for i in range(row1,row2+1):
            s+=self.subsumcal(i,col1,col2)
        return s
        



    def prefixcal(self,row:int)->List[int]:
        prefix=[]
        total=0
        for n in self.matrix[row]:
            total+=n
            prefix.append(total)
        return prefix
    def subsumcal(self,row:int,l:int,r:int)->int:
        prefix=self.prefixcal(row)
        return prefix[r] - (prefix[l-1] if l>0 else 0)
    
    

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)