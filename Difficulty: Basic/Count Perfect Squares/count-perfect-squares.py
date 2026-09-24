class Solution:
    def countSquares(self, n):
        # code here 
        count = 0
        for i in range(1, n):
            if (i*i < n):
                count = count + 1
            else:
                break
        return count