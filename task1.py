import timeit
from random import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

def timer(string, func, array):
    start = timeit.default_timer()
    print(string)
    func(array)
    
    print("Time consumed :", timeit.default_timer() - start)
    print("\n")

if __name__ == "__main__":
    arr = [int(random() * 100 + 1) for _ in range(10000)]
    arr2 = [int(random() * 100 + 1) for _ in range(1000)]

    timer("Merge sort of 1000 elements", merge_sort, arr)
    timer("Insertion sort of 1000 elements", insertion_sort, arr)
    timer("Timsort sort of 1000 elements", sorted, arr)

    print("_________________________")

    timer("Merge sort of 100 elements", merge_sort, arr2)
    timer("Insertion sort of 100 elements", insertion_sort, arr2)
    timer("Timsort sort of 100 elements", sorted, arr2)
