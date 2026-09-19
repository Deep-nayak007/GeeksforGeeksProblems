class Solution:
    def lastWordLen(self, s):
        # code here
        word = s.split()
        last = word[-1]
        output = len(last)
        return output