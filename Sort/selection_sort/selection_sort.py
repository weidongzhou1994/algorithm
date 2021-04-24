#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/24 19:04
# @Author  : Weidong Zhou
# @File    : selection_sort.py
# @Software: PyCharm

def find_samlllist(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_samlllist(arr)
        new_arr.append(arr.pop(smallest))
        # pop 既从 list 中删除了 smallest，同时又返回了 smallest
    return new_arr


print(selection_sort([5, 3, 6, 2, 10]))
