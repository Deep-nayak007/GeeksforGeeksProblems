class Solution:
    def searchInsertK(self, arr, k):
        # code here
        
        for i in range(len(arr)):
            if(arr[i] == k):
                return i
            elif(arr[i] >= k):
                return i
            else:
                x = i + 1
        return x        