a=int(input("Enter 3 values\na:"))
b=int(input("b:"))
c=int(input("c:"))

if a==b or a==c:
    print("Two values are definetly equal")
    if a == b and a == c:
        print("Three values are equal")
    else:
        print("Only Two values are equal")
else:
    print("Every value is different")

if a is not b:
    print("a and b are not equal")
else:
    print("a and b are equal")