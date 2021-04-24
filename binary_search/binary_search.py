#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/24 18:47
# @Author  : Weidong Zhou
# @File    : binary_search.py
# @Software: PyCharm


def binary_search(input_list, input_item):
    low = 0
    high = len(input_list) - 1
    while low <= high:
        mid = int((low + high) / 2)
        guess = input_list[mid]
        if input_item == guess:
            return mid
        if input_item > guess:
            low = mid - 1
        else:
            high = mid + 1
    return None


mylist = [1, 3, 5, 7, 9]
item = 5

print(binary_search(mylist, item))
