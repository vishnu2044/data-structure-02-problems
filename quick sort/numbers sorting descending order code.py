def sort_descending(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[0]
        left = []
        right = []
        for index in range(1, len(lst)):
            if pivot < lst[index]:
                left.append(lst[index])
            else:
                right.append(lst[index])
        return sort_descending(left) + [pivot] + sort_descending(right)

num_list = [10, 5, 67, 34, 90, 23, 68, 21, 89, 56]
result = sort_descending(num_list)
print(result)


