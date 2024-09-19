# Given a number n. Count the number of digits in n which evenly divide n. Return an integer, total number of digits of n which divides n evenly.

# Note :- Evenly divides means whether n is divisible by a digit i.e. leaves a remainder 0 when divided.

# Examples :
# Input: n = 12
# Output: 2
# Explanation: 1, 2 when both divide 12 leaves remainder 0.

def evenlyDivides(n):
    count = 0
    og_num = n   # Store the original number
    while n > 0:
        last_digit = n % 10    # Extract the last digit
        n = n // 10   # Remove the last digit from n

        # Check if the last digit is not zero and divides the original number
        if last_digit != 0 and og_num % last_digit == 0:
            count += 1
    return count    

num = int(input("Enter the number:"))

print(evenlyDivides(num))