def b_sort():
    nums = [23, 45, 87, 99, 105, 303, 404, 76, 502, 55, 606, 724, 1001]
    counter = 0
    print(nums)
    max = 12
    swap = True
    while swap is True:
        swap = False
        for x in range(0, max):
            if nums[x] > nums[x + 1]:
                temp = nums[x]
                nums[x] = nums[x + 1]
                nums[x + 1] = temp
                swap = True
        max = max - 1
        counter = counter + 1
    print(nums)
    print("Iterations of B_Sort : ", counter)


def i_sort():
    nums = [23, 45, 87, 99, 105, 303, 404, 76, 502, 55, 606, 724, 1001]
    print(nums)
    count = 0
    for x in range(0, 13):
        i = x
        temp = nums[x]
        while i > 0 and nums[i - 1] > temp:
            nums[i] = nums[i - 1]
            i = i - 1
            count = count + 1
        nums[i] = temp
    print(nums)
    print("Iterations of I_Sort : ", count)


b_sort()
print("---------------------------------------------")
i_sort()