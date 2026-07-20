def quick_sort(list_integers):
    if list_integers == []:
        return []
    if len(list_integers) == 1:
        return list_integers
    pivot = list_integers[0]
    copied_list = []
    less_than_pivot = []
    equal_pivot = []
    greater_than_pivot = []
    for integer in list_integers:
        copied_list.append(integer)
        if integer < pivot:
            less_than_pivot.append(integer)
        elif integer > pivot:
            greater_than_pivot.append(integer)
        else:
            equal_pivot.append(integer)
    less_than_pivot = quick_sort(less_than_pivot)
    greater_than_pivot = quick_sort(greater_than_pivot)
    l = len(less_than_pivot)
    e = len(equal_pivot)
    g = len(greater_than_pivot)
    copied_list[:l] = less_than_pivot[:]
    copied_list[l:l+e] = equal_pivot[:]
    copied_list[l+e:l+e+g] = greater_than_pivot[:]
    return copied_list