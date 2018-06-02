from timeit import default_timer as timer
from random import randint,uniform


def ssort(array):
    for i in range(len(array)):
        indxMax = i
        for j in range(i+1, len(array)):
            if array[j] > array[indxMax]:
                indxMax = j
        tmp = array[indxMax]
        array[indxMax] = array[i]
        array[i] = tmp
    return array


def ssortEnd(array):
    for i in range(len(array)-1,-1,-1):
        indxMin = i
        for j in range(i-1,-1,-1):
            if array[j] < array[indxMin]:
                indxMin = j
        tmp = array[indxMin]
        array[indxMin] = array[i]
        array[i] = tmp
    return array

def choice():
    print("|No|Sort Method|Type |Direction|Order")
    print("|1 |Selection  |Int  |Begin    |Descending|")
    print("|2 |Insertion  |Char |Begin    |Ascending |")
    print("|3 |Counting   |Int  |End      |Descending|")
    print("|4 |Bubble     |Char |End      |Ascending |")
    print("|5 |Counting   |Int  |Begin    |Descending|")
    print("|6 |Selection  |Int  |End      |Ascending |")
    print("|7 |Insertion  |Char |Begin    |Descending|")
    print("|8 |Bubble     |Int  |End      |Ascending |")
    print("|9 |Selection  |Float|Begin    |Descending|")
    print("|10|Counting   |Int  |End      |Ascending |")


def main():
    choice();
    arrayInt = [randint(-100,100) for i in range(10000)]
    arrayFloat = [round(uniform(-100,100),2) for i in range(1000)]
    sortMethod = input("Choose the sort method: ");
    if sortMethod == '1':
        start = timer()
        print(arrayInt)
        print(ssort(arrayInt));
        end = timer()
        print("Time: ", end - start,'s')
    elif sortMethod == '9':
        start = timer()
        print(arrayFloat)
        print(ssort(arrayFloat))
        end = timer()
        print("Time: ",end - start,'s')
    elif sortMethod == '6':
        print(arrayInt)
        print(ssortEnd(arrayInt))

main()
