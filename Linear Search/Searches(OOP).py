#Linear_Search using OOP
class Search:
    def __init__(self, myarray):
        self.myarray = myarray

    def linear_search(self, value):
        for i in range(len(self.myarray)):
            if self.myarray[i] == value:
                return i
        return -1

    def binary_search(self, value):
        found = False
        lower = 0
        upper = len(myarray)
        while lower <= upper and found == False:
            mid = (lower + upper) // 2
            if self.myarray[mid] == value:
                found = True
                return 1
            elif value > self.myarray[mid]:
                lower = mid + 1
            elif value < self.myarray[mid]:
                upper = mid - 1
        return -1

myarray = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Enter Value to Search? ")
value = int(input())
# array_data = Search(myarray)
# result = array_data.linear_search(value)
array_data = Search(myarray)
result = array_data.binary_search(value)

if result != -1:
    print("Value Found")
else:
    print("Value Not Found")