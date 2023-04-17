def sort(lst):
    if len(lst) <=1:
        return lst
    else:
        pivot = lst[0]
        left = []
        right = []
        for i in range(1, len(lst)):
            if pivot > lst[i]:
                left.append(lst[i])


            else:
                right.append(lst[i])
        return sort(left) + [pivot] + sort(right)


list = 'jjhgjytrex'
result = sort(list)
print(result)