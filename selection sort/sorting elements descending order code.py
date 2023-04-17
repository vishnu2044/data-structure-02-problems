lst = [1, 2, 21, 45, 3, 12, 5]
for j in range(len(lst)-1):
    max_val = j
    for i in range(j, len(lst)):
        if lst[max_val] < lst[i]:
            max_val = i
    lst[max_val], lst[j] = lst[j], lst[max_val]

print(lst)
