def concat_string():
    print("Enter String to Eliminate Spaces...")
    instring = input()
    mystring = ""

    for alphabet in instring:
        if alphabet != " ":
            mystring = mystring + alphabet
    print(mystring)
concat_string()