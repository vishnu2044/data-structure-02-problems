list1 = [67, 45, 12, 23, 56, 78, 1, 56, 234]
for j in range(len(list1)-1):
    minimum_value = j
    for i in range(j+1, len(list1)):
        if list1[minimum_value] > list1[i]:
            minimum_value = i

    temp = list1[minimum_value]
    list1[minimum_value] = list1[j]
    list1[j] = temp

print(list1)