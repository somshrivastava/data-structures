def bubble_sort(lst):
    for i in range(len(lst)-1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
    return lst

def selection_sort(lst):
    for i in range(len(lst)-1):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        if i != min_index:
            temp = lst[i]
            lst[i] = lst[min_index]
            lst[min_index] = temp
    return lst

def insertion_sort(lst):
    for i in range(1, len(lst)):
        temp = lst[i]
        j = i-1
        while temp < lst[j] and j > -1:
            lst[j+1] = lst[j]
            lst[j] = temp
            j -= 1
    return lst

def merge_sort(lst):
    def merge(lst1, lst2):
        combined = []
        i = 0
        j = 0
        while i < len(lst1) and j < len(lst2):
            if lst[i] < lst[j]:
                combined.append(lst1[i])
                i += 1
            elif lst[j] < lst[i]:
                combined.append(lst2[j])
                j += 1
        while i < len(lst1):
            combined.append(lst1[i])
            i += 1
        while j < len(lst2):
            combined.append(lst2[j])
            j += 1
        return combined
    if len(lst) == 1:
        return lst
    mid_index = int(len(lst) / 2)
    left = merge_sort(lst[:mid_index])
    right = merge_sort(lst[mid_index:])
    return merge(left, right)

def quick_sort_helper(lst, left, right):
    def pivot(lst, pivot_index, end):
        def swap(lst, index1, index2):
            temp = lst[index1]
            lst[index1] = lst[index2]
            lst[index2] = temp
        swap_index = pivot_index
        for i in range(pivot_index+1, end+1):
            if lst[i] < lst[pivot_index]:
                swap_index += 1
                swap(lst, swap, i)
        swap(lst, pivot_index, swap_index)
        return swap_index
    if left < right:
        pivot_index = pivot(lst, left, right)
        quick_sort_helper(lst, left, pivot_index-1)
        quick_sort_helper(lst, pivot_index+1, right)
    return lst

def quick_sort(lst):
    return quick_sort_helper(lst, 0, len(lst)-1)

