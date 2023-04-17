def sorting(list1):
    if len(list1) <= 1:
        return list1
    else:
        pivot = list1[0]
        left = []
        right = []
        for i in range(1, len(list1)):
            if list1[i] < pivot:
                left.append(list1[i])
            else:
                right.append(list1[i])
        return sorting(left) + [pivot] + sorting(right)


list = [5, 71, 72, 67, 45, 32, 19, 98]
result = sorting(list)
print(result)