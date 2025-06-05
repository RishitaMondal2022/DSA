class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l=[]
        for i in range(1,numRows+1):
            if i == 1:
                l.append([1])
            elif i == 2:
                l.append([1,1])
            else:
                l.append([0]*i)
                l[i-1][0]=1
                for j in range(i-2):
                    l[i-1][j+1] = l[i-2][j] +l[i-2][j+1]
                l[i-1][-1]=1

        return l