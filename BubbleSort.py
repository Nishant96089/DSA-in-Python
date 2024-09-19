def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

numList = list(map(int,input("Enter a list of numbers: ").split()))
bubbleSort(numList)
print(f"Sorted array: {numList}")