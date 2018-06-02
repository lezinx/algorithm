def quicksort(x):
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        midIndex = len(x)//2
        # first,last = x[-1],x[0]
        last = x[-1]
        # midIndex,last = x[-1],x[midIndex]
        pivot = last
        i = 0
        for j in range(len(x)-1):
            if x[j+1] < pivot:
                x[j+1],x[i+1] = x[i+1], x[j+1]
                i += 1
        x[0],x[i] = x[i],x[0]
        first_part = quicksort(x[:i])
        second_part = quicksort(x[i+1:])
        first_part.append(x[i])
        return first_part + second_part


with open('input_001_10000.txt') as file:
    alist = []
    for line in file:
        alist.append(int(line.strip()))
    alist.pop(0)

a = quicksort(alist)
print(a)
