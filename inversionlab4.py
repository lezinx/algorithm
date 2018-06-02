from collections import OrderedDict

def newOrder(a,b):
    dic = {int(i):int(j) for i,j in zip(a,b)}
    dic=OrderedDict(sorted(dic.items()))
    # for key in dic:
    #     print (key, dic[key])
    c = []
    for key in dic:
        c.append(dic[key])
    return c


def mergeSort(array):
    count = 0
    leftcount = 0
    rightcount = 0
    array2 = []
    if len(array) > 1:
       mid = len(array) // 2
       lefthalf = array[:mid]
       righthalf = array[mid:]
       leftcount, lefthalf = mergeSort(lefthalf)
       rightcount, righthalf = mergeSort(righthalf)

       i = 0
       j = 0

       while i < len(lefthalf) and j < len(righthalf):
         if lefthalf[i] < righthalf[j]:
             array2.append(lefthalf[i])
             i += 1
         else:
             array2.append(righthalf[j])
             j += 1
             count += len(lefthalf[i:])

       while i < len(lefthalf):
          array2.append(lefthalf[i])
          i += 1

       while j < len(righthalf):
          array2.append(righthalf[j])
          j += 1
    else:
        array2 = array[:]

    return count + leftcount + rightcount, array2

d = {}
with open('input_1000_5.txt') as file:
    for line in file:
        key, *value = line.split()
        d[key] = value

user1 = input('User No: ')
user2 = input('User1 No: ')
newUser = newOrder(d[user1],d[user2])
print(newUser)
print(d[user1],d[user2])
print(mergeSort(newUser))
