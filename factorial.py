# Write a program to calculate the factorial of a number using a for loop.
n = int(input("enter any number: "))
fact = 1
for i in range (1,n+1):
  fact = fact * i

print(fact)