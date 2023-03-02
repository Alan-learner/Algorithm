# encoding: utf-8
# author: Alan-learner

from typing import List
from heapq import heapify, heappop

"""
sort a array (List[dict]) by key_name.

Note:
1.build-in sort function is not allowed.
2.time complex is less than O(n^2).
3.if val is equal, stay original order.

"""


def convert(x: str) -> str:
    lst = x.split("/")
    lst = lst[::-1]
    y = "/".join(lst)
    return y


def heap_sort(nums: list) -> list:
    heapify(nums)
    sorted_nums = []
    while nums:
        num = heappop(nums)
        sorted_nums.append(num)
    return sorted_nums


def quick_sort(nums: list) -> list:
    length = len(nums)
    if length <= 1:
        return nums
    pivot = nums.pop()
    left = [val for val in nums if val <= pivot]
    right = [val for val in nums if val > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


def merge(sorted_nums1: list, sorted_nums2: list) -> list:
    sorted_nums = []
    while sorted_nums1 and sorted_nums2:
        if sorted_nums1[-1] >= sorted_nums2[-1]:
            target_num = sorted_nums1.pop()
        else:
            target_num = sorted_nums2.pop()
        sorted_nums.append(target_num)
    if sorted_nums1:
        sorted_nums.extend(sorted_nums1[::-1])
    if sorted_nums2:
        sorted_nums.extend(sorted_nums2[::-1])
    return sorted_nums[::-1]


def merge_sort(nums: list) -> list:
    length = len(nums)
    if length <= 1:
        return nums
    mid = length // 2
    sorted_nums1 = merge_sort(nums[:mid])
    sorted_nums2 = merge_sort(nums[mid:])
    sorted_nums = merge(sorted_nums1, sorted_nums2)
    return sorted_nums


def sort_algorithm(arr: List[dict], key: str, sort_algo=heap_sort) -> list:
    if key not in ["due_day", "priority", "complete_status"]:
        raise KeyError
    target_key = key
    if key == "complete_status":
        target_key = "status"
    tmp_list = []
    for idx, dic in enumerate(arr):
        if target_key == "due_day":
            tmp_list.append((convert(dic[target_key]), idx))
        else:
            tmp_list.append((dic[target_key], idx))
    tmp_list = sort_algo(tmp_list)  # O(n*log n)
    result = []
    for _, idx in tmp_list:
        result.append(arr[idx])
    return result


def main():
    res = sort_algorithm(arr=[{
        "task_name": "abc",
        "due_day": "11/05/2014",
        "priority": 2,
        "status": False
    }, {
        "task_name": "bcd",
        "due_day": "12/03/2013",
        "priority": 1,
        "status": True
    }, {
        "task_name": "cde",
        "due_day": "06/05/2017",
        "priority": 5,
        "status": False
    }, {
        "task_name": "def",
        "due_day": "02/05/2012",
        "priority": 0,
        "status": True
    }
    ], key="due_day",
        sort_algo=merge_sort)
    print(res)


if __name__ == '__main__':
    main()
