def strip_string():
    outstring = ""
    print("Enter String to Strip...")
    instring = input()

    for x in instring:
        if x != " ":
            outstring = outstring + x

    print(outstring)


strip_string()