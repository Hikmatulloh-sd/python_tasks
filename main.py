from time import time

"""
Оценка сложности О(n**2)
"""
def bubble_sort(arr):
    start = time()
    for _ in range(len(arr)):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    end = time()
    print(end - start)
    return arr

"""
Оценка сложности О(log(n))2

"""
def binary_search(arr,el):
    start = time()
    while arr:
        mid_index = (len(arr) // 2)
        mid_value = arr[mid_index]

        if mid_value == el:
            return arr[mid_index]

        elif mid_value > el:
            arr = arr[:mid_index]
        else:
            arr = arr[mid_index:]

    end = time()
    print(end - start)

    return None
