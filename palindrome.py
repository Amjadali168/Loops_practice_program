# Write a program to check if a given number is a palindrome using a while loop.
num = int(input("enter a number: "))
temp = num
reverse = 0
while temp > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp// 10
if num == reverse:
    print("It is palindrome number")
else:
    print("It is not palindrome number")