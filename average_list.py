# Write a program to calculate the average of a list of numbers using a for loop.
num_list = [1,2,3,4,5,6]
sum = 0
count = 0
for i in num_list:
    sum += i
    count += 1
avg = sum / count
print(avg)