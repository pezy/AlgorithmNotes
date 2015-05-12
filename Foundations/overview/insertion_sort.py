__author__ = 'pezy'


def insertion_sort(lst):
    for j in range(1, len(lst)):
        key = lst[j]
        i = j - 1
        while i >= 0 and lst[i] > key:
            lst[i + 1] = lst[i]
            i -= 1
        lst[i + 1] = key
    return lst


def insertion_sort_non_increasing(lst):
    for j in range(1, len(lst)):
        key = lst[j]
        i = j - 1
        while i >= 0 and lst[i] < key:
            lst[i + 1] = lst[i]
            i -= 1
        lst[i + 1] = key
    return lst


def linear_search(lst, v):
    for j in range(0, len(lst)):
        if v == lst[j]:
            return j
    return None


def add_binary(a_lst, b_lst):
    c_lst = [None]*(len(a_lst)+1)
    carry = 0
    for j in reversed(range(len(a_lst))):
        c_lst[j+1] = (a_lst[j] + b_lst[j] + carry) % 2
        carry = (a_lst[j] + b_lst[j] + carry) // 2
    c_lst[0] = carry
    return c_lst


def selection_sort(lst):
    for j in range(0, len(lst)-1):
        smallest = j
        for i in range(j+1, len(lst)):
            if lst[i] < lst[smallest]:
                smallest = i
        lst[j], lst[smallest] = lst[smallest], lst[j]
    return lst
