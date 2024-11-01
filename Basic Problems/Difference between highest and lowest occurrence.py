# User function Template for python3
from collections import defaultdict
class Solution:
    def findDiff(self, arr):
        # code here
        freq = defaultdict(int)
        for i in arr:
            freq[i] += 1
        max_freq_value = max(freq.values())
        min_freq_value = min(freq.values())

        max_freq = max(i for i in freq if freq[i] == max_freq_value)
        min_freq = min(i for i in freq if freq[i] == min_freq_value)

        return freq[max_freq] - freq[min_freq]