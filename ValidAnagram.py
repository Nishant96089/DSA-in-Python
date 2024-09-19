def validAnagram(a, b):
    if len(a) != len(b):
        return False
    
    check_a = {}
    check_b = {}

    for i in a:
        if i in check_a:
            check_a[i] += 1
        else:
            check_a[i] = 1

    for i in b:
        if i in check_b:
            check_b[i] += 1
        else:
            check_b[i] = 1

    return check_a == check_b                    

word1 = input("Enter first word:").lower()
word2 = input("ENter second word:").lower()

print(validAnagram(word1, word2))