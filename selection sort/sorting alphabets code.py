def sort(alps):
    for i in range(len(alps)-2):
        min_value = i
        for j in range(i+1, len(alps)):
            if alps[min_value] > alps[j]:
                min_value = j
        alps[i], alps[min_value] = alps[min_value], alps[i]


alps = ["h", "r", "a", "f", "d", "v", "e", "i"]

sort(alps)
print(alps)