def selection_sort(arr, n):
    for i in range(n - 1):
        mini = i
        for j in range(i + 1, n):
            if arr[j] < arr[mini]:
                mini = j
        arr[mini], arr[i] = arr[i], arr[mini]
    return arr


def bubble_sort(arr, n):
    swap = False
    for i in range(n - 1, -1, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True
        if not swap:
            break
        print("sorting is on progress")
    return arr


def insertion_sort(arr, n):
    swap = False
    for i in range(n):
        j = i
        while j != 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
            print("Swapping done!")

    return arr


def merge_sort(arr, low, high):
    if low == high:
        return
    mid = (low + high) // 2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid + 1, high)
    merge(arr, low, mid, high)


def merge(arr, low, mid, high):
    left = low
    right = mid + 1
    temp = []
    while (left <= mid) and (right <= high):
        if (arr[left] <= arr[right]):
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    while (left <= mid):
        temp.append(arr[left])
        left += 1
    while (right <= high):
        temp.append(arr[right])
        right += 1

    for i in range(low, high + 1):
        arr[i] = temp[i - low]


def quick_sort(arr, low, high):
    if low < high:
        partition = qs(arr, low, high)
        quick_sort(arr, low, partition - 1)
        quick_sort(arr, partition + 1, high)


def qs(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    while i < j:
        while arr[i] <= pivot and i <= high - 1:
            i += 1
        while arr[j] > pivot and j >= low + 1:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j


def recursive_bubble_sort(arr, n):
    if n == 1:
        return
    for j in range(n):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
    recursive_bubble_sort(arr, n - 1)


def recursive_insertion_sort(arr, n):
    if n == len(arr):
        return
    j = n
    while j != 0 and arr[j - 1] > arr[j]:
        arr[j - 1], arr[j] = arr[j], arr[j - 1]
        j -= 1
    recursive_insertion_sort(arr, n + 1)


arr = [1, 577, 5, 33, 55]
recursive_insertion_sort(arr, 0)
print(arr)