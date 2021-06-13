"""
This module implements binary search function
"""


def binary_search(item, search_list):
    """Implements binary search, returns index of element in list"""
    head_index = 0
    tail_index = len(search_list) - 1

    if not search_list:
        raise ValueError("The list is empty!")

    while head_index <= tail_index:
        middle_index = (head_index + tail_index) // 2
        supposed_item = search_list[middle_index]
        if supposed_item == item:
            print(f"Item: '{item}' ----> index: '{middle_index}")
            return item
        elif supposed_item < item:
            head_index = middle_index + 1
        else:
            tail_index = middle_index - 1
    raise ValueError(f"The item '{item}' is not in this list")


if __name__ == '__main__':
    ll = [312, 232, 679, 858, 3, 640, 519, 248, 860, 853,
          229, 491, 135, 14, 55, 21, 684, 853, 752, 978]
    ll = sorted(ll)
    print(ll)
    binary_search(491, ll)
    binary_search(858, ll)
    binary_search(3, ll)
    binary_search(978, ll)
    binary_search(1, ll)
