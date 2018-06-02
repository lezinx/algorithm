from random import randint


def bin_search(arr1,arr2):
    # x1 = 0;
    # x2 = len(arr1);
    for i in range(len(arr2)):
        x1 = 0;
        x2 = len(arr1);
        while x1 < x2 - 1:
            mid = (x1+x2)//2;
            if arr1[mid] > arr2[i]:
                x2 = mid;
            else:
                x1 = mid;
        if x1 >= 0 and arr1[x1] == arr2[i]:
            print(arr2[i] ,': YES')
        else:
            print(arr2[i] ,': NO')



N = int(input('N = '));
K = int(input('K = '));
array = sorted([randint(-5,10) for x in range(N)]);
array2 = sorted([randint(-5,10) for x in range(K)]);
print(array,'\n',array2);
print(bin_search(array,array2));
