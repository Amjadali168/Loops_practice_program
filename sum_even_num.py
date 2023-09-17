# Write a program to find the sum of all even numbers between 1 and 100 using a for loop.
sum = 0
for num in range(1,101):
       if num % 2 == 0:
        sum += num

# Print the sum of even numbers
print("Sum of even numbers between 1 and 100:", sum)

