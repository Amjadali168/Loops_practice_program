# Write a program to print the multiplication table of a given number using a while loop.
num = int(input("Enter any integer: "))

i = 1
while i <= 10:
    # result = num * i
    print(f"{num} x {i} = {num * i}")
    i += 1
