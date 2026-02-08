def preview(MyFile):
#Print First 5 Lines from a Text File
    x = 0
    with open(MyFile, "r") as file:
        for line in file:
            if x >= 5:
                break
            if line != "\n":
                print("Line : ", line, end="")
            else:
                print("File is Empty")
            x = x + 1


preview("C:/Users/mhass/Documents/MyFile.txt")