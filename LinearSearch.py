def linearSearch(arr, n):
    for i in range(len(arr)):
        if arr[i] == n:
            return i
    return -1    

numList = list(map(int,input("Enter the list of numbers: ").split()))
target = int(input("Enter number to search: "))

index = linearSearch(numList, target)
if index != -1:
    print(f"The number {target} is found at index {index}")
else:
    print(f"The number {target} is not found in the list.")