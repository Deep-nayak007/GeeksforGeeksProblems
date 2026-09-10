class Solution:
    def factorial(self, n: int) -> int:
        # code here
        output = 1
        for i in range(1, n + 1):
            output = output * i;
        return output 