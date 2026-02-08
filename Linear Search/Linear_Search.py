# Linear_Search

array_data = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]
print("Enter Number to search in Array(Data)")
valtosearch = int(input())


def linear_search(array_data, valtosearch):
    i = 0
    while i < len(array_data):
        if array_data[i] == valtosearch:
            return i
        else:
            i = i + 1
    return -1


result = linear_search(array_data, valtosearch)

if result == -1:
    print("Value NOT Found in Array(Data)")
else:
    print("Value Found in Array(Data)")