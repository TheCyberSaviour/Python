# 9618/21/M/J/23 Q3
def point_sys():

    print("Enter Amount Paid...")
    amount = input()
    str_amount = ""
    int_amount = 0
    fullstop = "."
    x = 0

    for x in amount:
        if x != fullstop:
            str_amount = str_amount + x
    int_amount = int(str_amount)

    if 0 <= int_amount <= 10:
        int_amount = int_amount * 5
        print("Points Earned : ", int_amount)
    elif 10 < int_amount <= 100:
        int_amount = int_amount * 7
        print("Points Earned : ", int_amount)
    elif int_amount > 100:
        int_amount = int_amount * 10
        print("Points Earned : ", int_amount)


point_sys()