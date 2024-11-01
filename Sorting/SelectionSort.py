 # Idea of the selection sort is to select the minimum & swap it, Compress the array accordingly

def selection_sort(arr,n):
     for i in range(n):
         mini = i
         for j in range(i+1,n):
             if arr[j] < arr[mini]:
                 mini = j
         # you also check mini != i before swapping!
         arr[mini],arr[i] = arr[i],arr[mini]
     return arr


if __name__ == '__main__':
    arr = [47,2,1,3,443,5]
    selection_sort(arr,len(arr))
    print(arr)