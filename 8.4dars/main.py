#    https://www.codewars.com/kata/56b4bae128644b5613000037/train/python

from collections import defaultdict


def repeat_sum(list_of_lists):
    count = defaultdict(int)

    for sublist in list_of_lists:
        unique_numbers = set(sublist)
        for num in unique_numbers:
            count[num] += 1

    result = sum(num for num, cnt in count.items() if cnt >= 2)
    return result


print(repeat_sum([[1, 2, 3], [2, 8, 9], [7, 123, 8]]))
print(repeat_sum([[1], [2], [3, 4, 4, 4], [123456789]]))
print(repeat_sum([[1, 8, 8], [8, 8, 8], [8, 8, 8, 1]]))
