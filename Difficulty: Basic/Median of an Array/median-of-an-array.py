class Solution:
    def findMedian(self, arr):
        #code here.
        arr.sort()
        n = len(arr)
        median = n // 2
        if (n % 2 != 0):
            return arr[median]
        else:
            return (arr[median] + arr[median-1])/2
        