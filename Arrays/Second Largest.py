def getSecondLargest(arr):
    # Code Here
    first = -1
    second = -1
    for i in range(len(arr)):
        if arr[i] > first:
            second = first
            first = arr[i]
        # if element is not equal to first and greater than second update the second value
        elif arr[i] != first and arr[i] > second:
            second = arr[i]
    return second

# Time complexity = O(n)
# Space complexity = O(1)