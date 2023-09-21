# Define the range of numbers for the multiplication table
start_num = 1
end_num = 5

for num in range(start_num, end_num + 1):
    print(f"Multiplication table for {num}: ")

    for i in range(1, 11):
        result = num * i
        print(f"{num} x {i} = {result}")

    print()
