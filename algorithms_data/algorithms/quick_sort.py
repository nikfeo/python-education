"""
This module implements quick sort algorithm
"""

from random import randint


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


def quick_sort_iter(sort_list):
    """ iterable quick sort """

    length = len(sort_list)
    if length <= 1:
        return sort_list

    # set boundaries of the list: low index and high index
    boundaries = [[0, length - 1]]
    while len(boundaries):
        # puts two values from boundaries list in list
        border = boundaries.pop()
        # defines low index and high index of the list from 'border'
        low, high = border
        # defines pivot index of low item
        pivot = low
        # puts data of item with pivot index into 'base_data'
        pivot_data = sort_list[pivot]
        # swapping pivot item data and low item data
        sort_list[pivot], sort_list[low] = sort_list[low], sort_list[pivot]

        item_idx = low
        first_idx = low + 1
        last_idx = high

        # checks intersection between first and last indexes
        while first_idx <= last_idx:
            if sort_list[first_idx] < pivot_data:
                flag = -1
            elif sort_list[last_idx] > pivot_data:
                flag = 1
            else:
                flag = 0

            if flag < 0:
                item_idx = first_idx
            else:
                # checks that last index bigger than first
                while last_idx > first_idx:
                    if sort_list[last_idx] < pivot_data:
                        flag = -1
                    elif sort_list[last_idx] > pivot_data:
                        flag = 1
                    else:
                        flag = 0

                    if flag < 0:
                        item_idx = first_idx
                        sort_list[last_idx], sort_list[first_idx] = \
                            sort_list[first_idx], sort_list[last_idx]
                        last_idx -= 1
                        break

                    last_idx -= 1
            first_idx += 1
        sort_list[low], sort_list[item_idx] = sort_list[item_idx], sort_list[low]
        if low < item_idx - 1:
            boundaries.append([low, item_idx - 1])
        if item_idx + 1 < high:
            boundaries.append([item_idx + 1, high])

    return sort_list


if __name__ == '__main__':
    test_list = [3, 6, 8, 3, 0, 2, 3, 5, 8, 10, 11, 1, 19]
    test_list_2 = []
    for i in range(100):
        value = randint(0, 500)
        test_list_2.append(value)
    print(quick_sort_rec(test_list))
    print(quick_sort_iter(test_list))
    print(quick_sort_rec(test_list_2))
    print(quick_sort_iter(test_list_2))
