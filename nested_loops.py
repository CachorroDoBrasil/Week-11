# nested loop = a loop within another loop
# Outer loop:
#   inner loop:
rows = int(input("enter a number of rows: "))
columns = rows = int(input("enter a number of columns: "))
symbol = input("Enter a symbol to use: ")

for rows in range(3):
    for columns in range(1, 10):
     print(symbol, end=" ")
    print()