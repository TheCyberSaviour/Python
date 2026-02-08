# Proc to Check whether the Triangle is Right-Angled Triangle

def IsRA():
    l_num = 0
    a = int(input(print("Enter Value 1: ")))
    b = int(input(print("Enter Value 2: ")))
    c = int(input(print("Enter Value 3: ")))

    if b < a and c < a:
        l_num = a
    elif a < b and c < b:
        l_num = b
    elif a < c and b < c:
        l_num = c

    l_num = l_num*l_num
    l_num = (b * b) + (c * c)

IsRA()