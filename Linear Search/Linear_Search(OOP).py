# OOP Linear_Search
class Linear_Search:
    def __init__(self, myarray):
        self.myarray = myarray

    def search(self, value):
        for i in range(len(self.myarray)):
            if self.myarray[i] == value:
                return i
        return -1


myarray = [10, 20, 30, 40, 50]
print("Enter Value to Search in Array...")
value = int(input())
array_data = Linear_Search(myarray)
result = array_data.search(value)

if result != -1:
    print("Value Found")
else:
    print("Value NOT Found")