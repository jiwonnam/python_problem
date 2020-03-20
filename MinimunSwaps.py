"""Whenever swaping two elements, at least one element can find the appropriate position
so time complexity is c*(the number of elements in wrong position)
the worst case is when all elements are in wrong position and time complexity is 'n'"""

'''def selectionSort(arr, n):
    count = 0
    for i in range(n):
        min_index = i
        for j in range(i, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            temp = arr[i]
            arr[i] = arr[min_index]
            arr[min_index] = temp
            count += 1
    return count'''

def minimumSwaps(arr):
    sort = []
    count = 0
    for i in range(len(arr)): # time complexity is n
        if i+1 == arr[i]:
            continue
        else:
            sort.append(i) # add index of elements that are in wrong position

    for j in sort: # check the element from first to end in 'sort' array and fix it consecutively
        if j+1 == arr[j]:
            continue
        else:
            while 1:
                temp = arr[arr[j]-1] # swap two elements to put in correct position
                arr[arr[j]-1] = arr[j]
                arr[j] = temp
                count += 1
                if arr[j] == j+1:
                    break
    return count


if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().rstrip().split())
    res = minimumSwaps(arr)
    print res

