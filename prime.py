# Write a program to check if a given number is prime or not using a while loop.
number = int(input("Enter a number: "))

# Initialize a variable to keep track of factors
factor_count = 0

# Initialize a counter
i = 1

# Use a while loop to check for factors
while i <= number:
    if number % i == 0:
        factor_count += 1
    i += 1

# Check if the number is prime
if factor_count == 2:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
