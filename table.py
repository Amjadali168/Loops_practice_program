# Write a program to print the multiplication table of a given number using a while loop.
num = int(input("Enter any integer: "))

# Initialize a counter
i = 1

# Use a while loop to print the multiplication table
while i <= 10:
    result = num * i
    print(f"{num} x {i} = {result}")
    i += 1
