class Solution:
    def search(self, arr, x):
        c=0
        for num in arr:
            c=c+1
            if num==x:
                return c-1
        return -1    