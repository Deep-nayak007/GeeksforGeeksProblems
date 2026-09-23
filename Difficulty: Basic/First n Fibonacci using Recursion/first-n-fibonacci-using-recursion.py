class Solution:
    def fibonacciNumbers(self, n: int) -> list[int]:
        # code here
        if n == 1:
            return [0]
        x = 0
        y = 1
        output = [x, y]
        
        for i in range(2, n):
            z = x + y
            output.append(z)
            
            x = y
            y = z
        return output    