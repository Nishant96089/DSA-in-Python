# Input: 153                                                         Input: 123
# Output: true                                                       Output: false
# Explanation:                                                       Explanation:
# 153 is a 3-digit number, and 153 = 1^3 + 5^3 + 3^3.                123 is a 3-digit number, and 123 != 1^3 + 2^3 + 3^3 = 36.

def checkArmstrong(n):
    check = 0   
    og_num = n  # STore the original number
    while n:
        digit = n % 10   #   Getting last digit from number
        n = n // 10      #   Removing the last digit
        check += digit ** 3  #  Adding each digit to check with cubic root

    return og_num == check        

num = int(input("Enter the number:"))
print(checkArmstrong(num))