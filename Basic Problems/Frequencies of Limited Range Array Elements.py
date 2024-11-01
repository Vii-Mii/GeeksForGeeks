from collections import defaultdict

class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        #  do modify in the given array
        freq = defaultdict(int)
        for i in arr:
            freq[i] += 1
        for i in range(1,N+1):
            arr[i-1] = freq[i]
        return arr