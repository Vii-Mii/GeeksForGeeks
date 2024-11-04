# Take a pivot
# Place it at the correct position of the array (Assume that the array sorted where you would place the pivot)
# Smaller to the left & larger to the right. (if you change large to the left and smaller to the right the array would get sorted in descending order)
# This is basically a divide & conquer algorithm.

# Recursion part - Base condition (there has to be at least two elements to do the divide)
def quick_sort(arr,low,high):
    if low < high:
        pIndex = partition(arr,low,high)
        quick_sort(arr,low,pIndex-1)
        quick_sort(arr,pIndex+1,high)

# Partitioning Part
def partition(arr,low,high):
    pivot = arr[low]
    i = low
    j = high
    while i < j:
        # Smaller should be placed left
        while arr[i] <= pivot and i <= high - 1:
            i += 1
        # Larger should be placed right
        while arr[j] > pivot and j >= low + 1:
            j -= 1
        # if the i didn't cross j swap it
        if i < j:
            arr[i],arr[j] = arr[j],arr[i]
    # placing pivot at correct position (which is j)
    arr[low],arr[j] = arr[j],arr[low]
    return j

arr = [9.8,3,4,5,61,1.2]
quick_sort(arr,0,len(arr)-1)
print(arr)