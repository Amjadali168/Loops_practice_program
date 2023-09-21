# Write a program to count the number of vowels in a given string using a for loop.
input_string = input("Enter a string: ")
vowel_count = 0
vowels = "AEIOUaeiou" 

for char in input_string:
    if char in vowels:
        vowel_count += 1

print("The number of vowels in the string is:", vowel_count)
