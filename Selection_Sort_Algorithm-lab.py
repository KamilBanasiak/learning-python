def selection_sort(list_numbers):
    if list_numbers == []:
        return list_numbers
    if len(list_numbers) == 1:
        return list_numbers
    for i in range(len(list_numbers) - 1):
        minimal = min(list_numbers[i:])
        index = list_numbers.index(minimal, i)
        if i != index:
            list_numbers[i], list_numbers[index] = list_numbers[index], list_numbers[i]
    return list_numbers        