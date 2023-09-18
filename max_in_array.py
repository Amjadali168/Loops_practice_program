# Write a program to find the largest element in an array using a for loop.
num_elements = int(input("Enter the number of elements: "))

arr = []
for _ in range(num_elements):
    element = float(input("Enter element: "))
    arr.append(element)

largest = max(arr)

print(f"The largest element in the array is: {largest}")
