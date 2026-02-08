def main():
    Names = ["Hello", "world", "PKR", "USD", "CAD", "EUR"]
    NameToSearch = ""
    found = False
    x = 0

    print("Enter Name to Search")
    NameToSearch = input()

    for x in range(len(Names)):
        if NameToSearch == Names[x]:
            found = True
            break

    if found is True:
        print("Name Found...")
        print(x)
    else:
        print("Name NOT Found...")


main()