#Binary Search Different Algorithms

def Binary_Search_2(valtofind):
    global ArrayData
    count = 0
    First = 0
    Last = len(ArrayData)
    found = False
    while Last >= First and found == False:
        Mid = ((First + Last) // 2)
        if valtofind == ArrayData[Mid]:
            found = True
            print("Count :", count)
            return ("Value was Found on :", Mid)
        elif valtofind < ArrayData[Mid]:
            Last = Mid - 1
            count = count + 1
        elif valtofind > ArrayData[Mid]:
            First = Mid + 1
            count = count + 1
    print("Count :", count)
    return ("Value NOT Found")

ArrayData = [22, 25, 31, 32, 37, 39, 42, 47, 75, 101]
valtofind = int(input("Please Enter Value to Find..."))
result = Binary_Search_2(valtofind)
print(result)