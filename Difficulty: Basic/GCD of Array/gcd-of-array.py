import math
class Solution:
    def gcd(self, n, arr):
        # code here 
        x = arr[0]
        for i in range(1, n):
            x = math.gcd(x, arr[i])
        return x    