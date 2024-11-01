# Takes an element and place it at the correct position

def insertion_sort(arr,n):
    for i in range(n):
        j = i
        while (j > 0 and arr[j-1] > arr[j]):
            arr[j-1],arr[j] = arr[j],arr[j-1]
            j -= 1


if __name__ == '__main__':
    arr = [1,4,67,0,3,5]
    insertion_sort(arr,len(arr))
    print(arr)