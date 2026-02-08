def Create_File():
    Names = ["Hassan", "Aliha", "HN", "AH"]
    with open("C:/Users/mhass/Documents/MyFile.txt", "w") as file:
        for name in Names:
            file.write(name + "\n")
    print("your Data is Entered to MyFile.txt")


Create_File()