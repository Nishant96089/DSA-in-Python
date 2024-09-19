def containsDuplicate(arr):
    check = set()

    for i in arr:
        if i in check:
            return True
        else:
            check.add(i)
    return False        

numList = list(map(int,input("Enter list of numbers:").split()))
print(containsDuplicate(numList))