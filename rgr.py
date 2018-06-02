def readFromFile(text):
    dic = {}
    with open(text) as file:
        for line in file:
            key, *value = line.split()
            dic[key] = value
    return dic

def selectionSort(A):
    for i in range(len(A)):
        min_idx = i
        for j in range(i + 1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]
    return A


def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    while first <= last:
        i = (first + last) // 2
        if alist[i] == item:
            return item
        elif alist[i] > item:
            last = i - 1
        elif alist[i] < item:
            first = i + 1
        else:
            return None


def getKey(d, value):
    """Get dict key from a value"""
    keys = []
    for *k, v in d.items():
        if v[0] == value:
            keys.append(k[0])
    return keys

def main():
    d = readFromFile("rgr.txt")
    d = {int(k):v for k,v in d.items()}
    l = list(d.keys())
    l = selectionSort(l)
    for i in l:
        print(i,"-",d[i])
    findInfo = str(input("Введите дату вашего заказа : "))
    for i in getKey(d,findInfo):
        print(i,'-',d[i])

if __name__ == "__main__":
    main()






