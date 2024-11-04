def searchInSorted(arr, k):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == k:
            return True
    return False

# Time complexity : O(n) Basic Linear search
# Space complexity : O(1)