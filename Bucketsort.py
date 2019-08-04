#Python program to sor t an array
#using bucket sort

def insertionSort(b) :
    for i in range(1, len(b)):
        up = b[i]
        j = i-1
        while j>=0 and b[j] >up:
            b[j+1] = b[j]
            j-=1
        b[j+1] = up
    return b
def bucketSort(x):
    arr = [ ]
    slot_num = 10
    for i in range(slot_name):
        arr.append([])

    for j in x:
        index_b = int(slot_num * j)
        arr[index_b].append(j)


    for i in range(slot_num):
        arr[i] = insertionSort(arr[i])



    k=0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k+=1
        return x
#Driver code
x = [45,54,32,87,15,45]
print("Sorted Array is :\n")
print(bucketSort(x))
