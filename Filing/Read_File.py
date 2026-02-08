def Read_File():
    with open("C:/Users/mhass/Documents/MyFile.txt", "r") as file:
        for line in file:
            print(line)
    print("data ended")


Read_File()