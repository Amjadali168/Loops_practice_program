# Write a program to check if a given number is a perfect square using a while loop.
number = int(input("Enter a number: "))

odd_int = 1  # Initialize the first odd integer
square = 1    # Initialize the square as 1

while square < number:
    odd_int += 2   # Increment the odd integer by 2 in each iteration
    square += odd_int


if square == number:
    print(f"{number} is a perfect square.")
else:
    print(f"{number} is not a perfect square.")
