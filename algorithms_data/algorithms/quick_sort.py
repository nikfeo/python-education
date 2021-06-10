"""
This module implements quick sort algorithm
"""


def quick_sort_rec(sort_list):
    if len(sort_list) <= 1:
        return sort_list
    pivot = sort_list[len(sort_list) // 2]
    left_side = []
    mid_side = [i for i in sort_list if i == pivot]
    right_side = []
    for i in sort_list:
        if i < pivot:
            left_side.append(i)
        elif i > pivot:
            right_side.append(i)

    return quick_sort_rec(left_side) + mid_side + quick_sort_rec(right_side)


if __name__ == '__main__':
    test_list = [3, 6, 8, 3, 0, 2, 3, 5, 8, 10, 11, 1, 19]
    print(quick_sort_rec(test_list))
