def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]        


numList = list(map(int,input("Enter a list of numbers: ").split()))
selectionSort(numList)
print(f"Sorted array: {numList}")