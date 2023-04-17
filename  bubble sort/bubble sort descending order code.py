lst = list()
limit = int(input("Enter the limit : "))
for i in range(limit):
    x = int(input("Enter the value : "))
    lst.append(x)

for i in range(len(lst)-1):
    for j in range(len(lst)-i-1):
        if lst[j] < lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
print("The sorted list(in descending order) : ", lst)