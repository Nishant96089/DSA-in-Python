# A prime number is a positive integer that is divisible by exactly 2 integers, 1 and the number itself.

# Sample Input :
# 5
# Sample Output :
# YES

# Explanation of sample input :
# 5 is only divisible by 1 and 5. 2, 3 and 4 do not divide 5.

def checkPrime(n):
    if n <= 1:
        return 'NO'
    if n == 2:
        return 'YES'
    
    # Iterating from 2 to n and checking divisibility
    i = 2
    while i*i <= n:   # Checking up to square root of n
        if n % i == 0:
            return 'NO'
        i += 1
    return 'YES'    

num = int(input("Enter number:"))
print(checkPrime(num))