#Largest Number
print("Enter Number 1...")
a = int(input())
print("Enter Number 2...")
b = int(input())
print("Enter Number 3...")
c = int(input())

if a > b and a > c:
    print("A is Largest Number")
elif b > a and b > c:
    print("B is Largest Number")
elif c > a and c > b:
    print("C is Largest Number")