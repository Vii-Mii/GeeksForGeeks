# It pushes the maximum element to the last by the adjacent swaps

def bubble_sort(arr,n):
    swap = False
    for i in range(n-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swap = True
        if not swap:
            break
        print("swap done!")
    return arr

if __name__ == '__main__':
    # arr = [47, 2, 1, 3, 443, 5]
    arr = [1,2,3,4,5,6]
    bubble_sort(arr, len(arr))
    print(arr)