def FiletoArray(OldFile, MyArray):
    FileHandle = open("C:/Users/mhass/Documents/OldFile.txt", "r")
    for line in FileHandle:
        MyArray.append(line)
    FileHandle.close()


MyArray = []
FiletoArray("C:/Users/mhass/Documents/OldFile.txt", MyArray)
for x in MyArray:
    print(x, end="")