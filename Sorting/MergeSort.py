# the intuition of this sorting is to divide and merge

# Recursion part (divide,divide,divide & divide)
def merge_sort(arr,low,high):
    if low == high:
        return
    mid = (low + high) // 2
    merge_sort(arr,low,mid)
    merge_sort(arr,mid+1,high)
    merge(arr,low,mid,high)

# Merging part (merge,merge,merge & merge)
def merge(arr,low,mid,high):
    left = low
    right = mid+1
    temp = []
    # merging two sorted arrays
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    # Adding all the elements from left if present
    while left <= mid:
        temp.append(arr[left])
        left += 1
    # Adding all the elements from right if present
    while right <= high:
        temp.append(arr[right])
        right += 1
    # transferring the element from temp to actual array(arr)
    for i in range(low,high+1):
        arr[i] = temp[i-low]

arr = [3,1,6,22,2,4,9,10,12]
merge_sort(arr,0,len(arr)-1)
print(arr)