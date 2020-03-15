list_num = list(map(int, input("Enter the list : ").split(",")))
length = len(list_num)
list_total = []

for i in range(0, length):
    for x in range(i + 1, length):
        first = list_num[i]
        second = list_num[x]
        fab_list = [first, second]
        for y in range(x + 1, length):
            if first + second == list_num[y]:
                fab_list.append(list_num[y])
                first = second
                second = list_num[y]
        if len(list_total) < len(fab_list):
            list_total = fab_list
if len(list_total) > 2:
    print("The  Expected Output is :", list_total)
else:
    print("-1")
