def lenOfLongestSubarr(arr, k):
    # code here
    val = 0
    for i in range(len(arr)):
        summ = 0
        for j in range(i, len(arr)):
            summ += arr[j]
            if summ == k:
                val = max(val, j - i + 1)

    return val

# Brute force approach
# Time complexity : O(n2)
# Space complexity : O(1)
