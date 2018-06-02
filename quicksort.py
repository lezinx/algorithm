import time


time_start = time.clock()
def Quicksort(A,start,end):
    if start<end:
        pivot = Partition(A,start,end)
        Quicksort(A,start,pivot-1)
        Quicksort(A,pivot+1,end)
    return A


count = 0
def Partition(A,start,end):
    global count
    pivot = A[start]
    border = start
    for i in range(start,end+1):
        if A[i]<pivot:
            border+=1
            count += 1
            A[i],A[border] = A[border],A[i]
    A[start],A[border] = A[border],A[start]

    return border

# A=[]
# file = open("input__1000.txt","r")
# for line in file:
#     line.split(" ")
#     for i in line.split(" "):
#         i = int(i)
#     A.append(i)
# print(A)
with open('input__1000.txt') as file:
    A = []
    for line in file:
        A.append(int(line.strip()))
    A.pop(0)
print(Quicksort(A,0,len(A)-1))
print(count)
time_end = time.clock() - time_start
print(time_end)
