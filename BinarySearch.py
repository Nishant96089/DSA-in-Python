#  Binary search works correctly only if the array is sorted.
#  If you want to perform a searching algorithm on an unsorted array, then use Linear Search.

def binarySearch(arr, n):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < n:
            left = mid + 1
        elif arr[mid] > n:
            right = mid - 1
        else:
            return mid
    return -1            


numList = list(map(int,input("Enter list of numbers: ").split()))
numList.sort()  # Sorting the array after taking input
target = int(input("Enter number to search in the list: "))

index = binarySearch(numList, target)
print(f"Sorted Array: {numList}")
if index != -1:
    print(f"The number {target} is found at index {index}")
else:
    print(f"The number {target} is not found in the list.")    