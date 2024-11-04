from typing import List

def largest(arr: List[int]) -> int:
    maxx = float("-inf")
    for i in range(len(arr)):
        if arr[i] > maxx:
            maxx = arr[i]

    return maxx

# Time complexity = O(n)
# Space complexity = O(1)
