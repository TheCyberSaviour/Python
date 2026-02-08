def Last_Lines(MyFile):
    #Print Last 3 Lines from a Text File
    with open(MyFile) as file:
        LineX, LineY, LineZ = "", "", ""
        for line in file:
            LineZ = LineY
            LineY = LineX
            LineX = line

    print(LineZ, end="")
    print(LineY, end="")
    print(LineX)


Last_Lines("C:/Users/mhass/Documents/MyFile.txt")