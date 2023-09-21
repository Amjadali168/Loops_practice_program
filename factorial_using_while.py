# Write a program to find the factorial of a number using a while loop.
number = int(input("Enter a number: "))

factorial = 1  # Initialize the factorial to 1
current_num = 1  # Initialize the current number for multiplication

while current_num <= number:
    factorial *= current_num
    current_num += 1

print(f"The factorial of {number} is: {factorial}")
