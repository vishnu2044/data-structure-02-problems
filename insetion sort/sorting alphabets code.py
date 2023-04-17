def sort_alphabets(alp_list):

    for index in range(1, len(alp_list)):
        current_val = alp_list[index]
        pos = index
        while current_val < alp_list[pos-1] and pos >0:
            alp_list[pos] = alp_list[pos-1]
            pos -=1
        alp_list[pos] = current_val

    print(alp_list)


alp_list = ["g", "j", "d", "v", "e", "a", "n"]
sort_alphabets(alp_list)