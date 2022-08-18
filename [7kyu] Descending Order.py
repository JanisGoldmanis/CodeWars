# https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python

# While solution works, should have used Pythons inbuilt sort functionality. Easily compressible to understandable
# one-liner.

def descending_order(num):
    """
    :param num: non-negative integer
    :return: rearranged numbers to generate maximum possible number
    """
    string_num = str(num)
    map_object = map(int, string_num)
    separate_digit_list = list(map_object)
    while True:
        change = 0
        for index in range(len(separate_digit_list) - 1):
            if separate_digit_list[index] < separate_digit_list[index + 1]:
                separate_digit_list[index], separate_digit_list[index + 1] = separate_digit_list[index + 1], \
                                                                             separate_digit_list[index]
                change += 1
        if change == 0:
            return int("".join(map(str, separate_digit_list)))


if descending_order(1) == 1:
    print('1 is ok')
else:
    print('1 is not ok')
if descending_order(3671) == 7631:
    print('3671 is ok')
else:
    print('3671 is not ok')
