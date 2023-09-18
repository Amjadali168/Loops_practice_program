# Write a program to print the ASCII values of all uppercase letters using a for loop.

alphabet = input("Alphabet: ")

if len(alphabet) == 1 and alphabet.isalpha():
    ascii_value = ord(alphabet)
    print(f"ASCII value of '{alphabet}' is {ascii_value}")
else:
    print("Invalid input. Please enter a single alphabet character.")


