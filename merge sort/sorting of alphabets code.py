def merging_sorted(lst):
    if len(lst) <=1:
        return lst
    mid = len(lst) //2
    left = lst[mid:]
    right = lst[:mid]
    left = merging_sorted(left)
    right = merging_sorted(right)

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

        result += left[i:]
        result += right[j:]
        return result


lst = ["g", "s", "t", "a", "v", "n", "d"]
print(merging_sorted(lst))