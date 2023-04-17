def inssertion_sorting(num_list):
    for index in range(1, len(num_list)):
        current_element = num_list[index]
        pos = index
        while current_element < num_list[pos-1] and pos >0:
            num_list[pos] = num_list[pos-1]
            pos -= 1
        num_list[pos] = current_element

list = [6, 9, 2, 1, 7, 4]
inssertion_sorting(list)
print(list)