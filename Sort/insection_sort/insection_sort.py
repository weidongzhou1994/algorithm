#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/24 22:38
# @Author  : Weidong Zhou
# @File    : insection_sort.py
# @Software: PyCharm

def insection_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key
    return arr

print(insection_sort([5, 3, 6, 2, 10]))
