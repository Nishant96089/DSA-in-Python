# Given an integer x, return true if x is a palindrome, and false otherwise.

# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

def isPalindrome(x):
    og_num = x   # Store the original number
    reversed_x = 0

    if x < 0:
        return False
    
    while x > 0:
        last_digit = x % 10   # Extract the last digit
        reversed_x = reversed_x * 10 + last_digit  # adding the last digit of x to reversed_x sequentially
        x = x // 10  # removing last digit of x

    if og_num == reversed_x:
        return True
    else:
        return False

num = int(input("Enter the number:"))

print(isPalindrome(num))