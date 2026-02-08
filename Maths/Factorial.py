#Factorial

def my_fact(value):
    res = 1
    for i in range(1, value + 1):
        res = res * i
    return res


print("Enter Number to find Factorial...")
val = int(input())
print(my_fact(val))