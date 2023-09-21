# Write a program to find the smallest element in an array using a while loop.
num_elements = int(input("Enter the number of elements: "))

arr = []
for _ in range(num_elements):
    element = input("Enter element: ")
    arr.append(element)

smallest = min(arr)

print(f"The smallest element in the array is: {smallest}")