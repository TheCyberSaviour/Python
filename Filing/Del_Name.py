def del_name(OldFile, NewFile, Del_Name):
#Read Names from OldFile and Write in NewFile
#Take a Name as a parameter and DO NOT Include it in NewFile

    Name, Email = "", ""
    RecCopied, RecFound = 0, 0

    r_file = open(OldFile, "r")
    w_file = open(NewFile, "w")
    for line in r_file:
        if line != "\n":
            Name = line
            Email = r_file.readline()
            RecFound = RecFound + 1
            if Name != Del_Name + "\n":
                w_file.write(Name)
                w_file.write(Email)
                RecCopied = RecCopied + 1
    r_file.close()
    w_file.close()
    print(f"File {OldFile} contained {RecFound} employee details")
    print(f"{RecCopied} employee details were written to the File {NewFile}")


print("Enter Name...")
Del_Name = input()
del_name("C:/Users/mhass/Documents/OldFile.txt", "C:/Users/mhass/Documents/NewFile.txt", Del_Name)
