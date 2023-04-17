list1 = list()
limit = int(input("Enter the limit : "))
for i in range(limit):
    x = int(input("Enter the value : "))
    list1.append(x)

for i in range(len(list1)-1):
    for j in range(len(list1)-i-1):
        if list1[j] > list1[j+1]:
            list1[j], list1[j+1] = list1[j+1], list1[j]

print("The sorted list : ", list1)