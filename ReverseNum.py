# Example 1:                              Example 2:
# Input: n = 123                          Input: n = -123
# Output: 321                             Output: -321

def reverse(n):
    neg_num = False  # At first we don't know whether the number is negative or not

    if n < 0:
        neg_num = True  # Set the value True if negative
        n = -n  # Making it positive so that it can be reversed

    reversed_n = 0

    while n != 0:
        last_digit = n % 10  # Extract last digit of n
        reversed_n = reversed_n * 10 + last_digit   # adding the last digit to the reversed_n sequentially
        n = n // 10  # remove last digit from n

    if neg_num:
        reversed_n = -reversed_n   # making the number positive to negative again after reversing.

    return reversed_n        

num = int(input("Enter the number: "))

print(reverse(num))