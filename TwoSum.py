def twoSum(arr, n):
    ans = []

    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == n:
                ans = [i,j]
    return ans            

numList = list(map(int,input("Enter list of numbers:").split()))
target = int(input("Enter number:"))

print(twoSum(numList, target))