choice = int(input("Choose operation\nEnter 1 for addition\nEnter 2 for substraction\nEnter 3 for multiplication\nEnter 4 for division\n"))
a = int(input("Enter 2 numbers\na:"))
b = int(input("b:"))

if choice == 1:
    print(a + b)
elif choice == 2:
    print(a - b)
elif choice == 3:
    print(a * b)
elif choice == 4:
    print(a / b)
