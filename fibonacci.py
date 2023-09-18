# Write a program to print the Fibonacci series up to a given limit using a while loop.
# num = int(input("enter any number: "))
# n1,n2 = 0,1
# sum = 0
# for i in range(num):
#         print(sum,end=" ")
#         n1 = n2
#         n2 = sum
#         sum = n1 + n2
# print(sum)

num = int(input("Enter any number: "))
n1, n2 = 0, 1

if num <= 0:
    print("Invalid input. Please enter a positive integer.")
else:
    print("Fibonacci Series:")
    for _ in range(num):
        print(n1, end=" ")
        n1, n2 = n2, n1 + n2
