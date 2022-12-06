def find_max():
    numbers = [2, 4, 5, 7]
    max_num = numbers[0]
    for num in numbers:
        if max_num < num:
            max_num = num
    print(max_num)

