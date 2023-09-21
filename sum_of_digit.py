# Write a program to calculate the sum of digits of a number using a for loop.
num = int(input("Enter the number: "))
sum_of_digits = 0

number_str = str(num)

for digit in number_str:
    sum_of_digits += int(digit)
print("The sum of digits is:", sum_of_digits)
