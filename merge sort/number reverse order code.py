# number in reverse order
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            j +=1
    result += left[i:]
    result += right[j:]
    return result


lst = [5, 2, 12, 4, 3, 8, 21, 81, 56, 1]

print(merge_sort(lst))