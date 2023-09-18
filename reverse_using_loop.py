# Write a program to reverse a given string using a while loop.
string = input("Enter a string: ")
reversed_string = ""
index = len(string) - 1

while index >= 0:
    reversed_string += string[index]
    index -= 1

print("reversed string: ",reversed_string)