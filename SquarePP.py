num = int(input("Enter the number : \t"))
counter = 0
for i in range(0,num):
    for j in  range(0,i+1):
        print(counter,end=" ")
        counter = 2**(i+1)
    print()
