def insertion_descending(num_list):
    for index in range(len(num_list)):
        current_value = num_list[index]
        pos = index
        while current_value > num_list[pos -1] and pos >0:
            num_list[pos] = num_list[pos-1]
            pos -= 1
        num_list[pos] = current_value


list1 = [6, 8, 2, 4, 8, 1, 0, 2, 4]
insertion_descending(list1)
print(list1)